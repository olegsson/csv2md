__version__ = '0.0.1'

def csv2md(csv, delim=',', headers=True, padding=True):
    data = [
        x.split(delim) for x in csv.split('\n')
    ]
    if padding:
        widths = [
            max(
                len(x) for x in col
            ) for col in zip(*data)
        ]
    else:
        widths = [1 for x in data[0]]
    markdown = ''
    for i, row in enumerate(data):
        nrow = row
        if padding:
            nrow = []
            for j, val in enumerate(row):
                nrow.append(' %s%s '%(
                    val,
                    ' '*(widths[j]-len(val)),
                ))
        markdown += '|%s|\n'%'|'.join(nrow)
        if i == 0 and headers:
            markdown += '|%s|\n'%'|'.join(('-'*(w+2) for w in widths))
    return markdown

__all__ = ['csv2md']
