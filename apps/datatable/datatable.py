from django.db.models import Q
from datetime import datetime


class DataTableFilter():

    def __init__(self, request, table, columns, where, order):
        self.data = list()
        self.create_filter(request, table, columns, where, order)

    def column_filter(self, item, column):
        for elem in column.split('.'):
            try:
                item = getattr(item, elem)
            except AttributeError:
                return None
        return item

    def create_filter(self, request, table, columns, where, order):
        start = int(request.POST.get('start', 0))
        end = int(request.POST.get('length', 5))

        search_col = list()
        for idx, column in enumerate(columns):
            value = request.POST.get(
                "columns[" + str(idx) + "][search][value]", None)
            search_col.append(value)

        search = {}
        for idx, column in enumerate(columns):
            try:
                if search_col[idx]:
                    item = str(column['cl']).replace('.', '__')
                    contains = item + '__contains'
                    search[contains] = search_col[idx]

            except IndexError:
                print("erro")

        items = table.objects.filter(**search, **where).order_by(*order)[start:start+end]
        total = table.objects.filter(**search, **where).count()

        data = list()
        for item in items:
            arr = list()
            for column in columns:
                dados = self.column_filter(item, column['cl'])

                if column['type'] == 'str':
                    arr.append(dados)
                elif column['type'] == 'date':
                    if dados:
                        arr.append(dados.strftime("%d/%m/%Y"))
                    else:
                        arr.append(None)

            data.append(arr)

        self.data = {
            'recordsTotal': total,
            'recordsFiltered': total,
            'data': data,
        }


class DataTableRaw():

    def __init__(self, request, table, columns, query, where, value_where, group_by):
        self.data = list()
        self.create_raw(request, table, columns, query, where, value_where, group_by)

    def column_filter(self, item, column):
        for elem in column.split('.'):
            try:
                item = getattr(item, elem)
            except AttributeError:
                return None
        return item

    def create_raw(self, request, table, columns, query, where, value_where, group_by):
        start = int(request.POST.get('start', 0))
        end = int(request.POST.get('length', 5))

        search_col = list()
        for idx, column in enumerate(columns):
            value = request.POST.get(
                "columns[" + str(idx) + "][search][value]", None)
            search_col.append(value)

        search = list()
        for idx, value in enumerate(search_col):
            if value:
                search.append(columns[idx] + ' LIKE %s')
                array_value = ['%' + value + '%']
                value_where.extend(array_value)

        search = ' AND '.join(search)

        if where:
            if search:
                where = ' WHERE ' + where + ' AND ' + search
            else:
                where = ' WHERE ' + where
        else:
            if search:
                where = ' WHERE ' + search
            else:
                where = ''

        query = str(query) + str(where)

        if group_by:
            query = str(query) + str(group_by)

        print(query)

        items = table.objects.raw(query, value_where)[start:start+end]
        total = len(table.objects.raw(query, value_where))

        data = list()
        for item in items:
            arr = list()
            for column in columns:
                arr.append(
                    self.column_filter(item, column)
                )
            data.append(arr)

        self.data = {
            'recordsTotal': total,
            'recordsFiltered': total,
            'data': data,
        }
