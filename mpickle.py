from common.util import Alphabet,ETag,ConstTag

def encode_weight(w):
    if w is None:
        return '(None)'

    out = '(list ['
    for x in w:
        out += encode_numpy(x) + ', '
    return out + '])'

def encode_numpy(array):
    if array is None:
        return '(None)'

    out = '(np.array '
    out += 'shape=' + str(array.shape) + ' '
    out += 'dtype=' + str(array.dtype) + ' '

    out += '['
    flat = array.flatten()
    for x in flat:
        out += str(x) + ', '
    return out + '])'

def encodeUnicodeString(uniString):
    out = ''
    for i in uniString:
        out += str(ord(i)) + ', '
    return out

def decodeUnicodeString(uniString):
    out = unicode('')
    ar = uniString.split(', ')
    for i in ar:
        if i is not '':
            out += unichr(int(i))
    return out

def encodeType(data):
    if data is None:
        return '(None)'

    if type(data) is unicode:
        y = encodeUnicodeString(data)
        return '(unicode ' + y + ')'

    elif type(data) is ETag:
        return '(etag ' + data + ')'

    elif type(data) is ConstTag:
        return '(constTag ' + data + ')'

    elif type(data) is str:
        # The feature code books have text that they mark as unicode but
        # since were not unicode anymore we need to convert it, hopefully this
        # wont polute anything else
        if 'u\'' in data:
            # print('-----------')
            # print(data)
            # print(data.replace('u\'', '\''))
            # print('-----------')
            data = data.replace('u\'', '\'')

        return '(string ' + data + ')'

    elif type(data) is int:
        return '(int ' + str(data) + ')'

    else:
         raise Exception('Unknown token table type: ' + str(type(x)))

def encode_token_table(dd):
    if dd is None:
        return '(None)'

    out = '(defaultdict '
    out += 'type= ' + 'set' + ' '

    out += '{'
    for k, v in dd.iteritems():
        out += '\'' + str(k) + '\': ['
        for x in v:

            y = encodeType(x)
            out += y + ', '
            # if type(x) is unicode:
            #     y = encodeUnicodeString(x)
            #     out += '(unicode ' + y + ')'
            #
            # elif type(x) is ETag:
            #     out += '(etag ' + x + ')'
            #
            # elif type(x) is ConstTag:
            #     out += '(constTag ' + x + ')'
            #
            # elif type(x) is str:
            #     out += '(string ' + x + ')'
            #
            # else:
            #      raise Exception('Unknown token table type: ' + str(type(x)))
        out += '], '
    return out + '})'

def encode_pp_count_dict(dd):
    if dd is None:
        return '(None)'

    out = '(defaultdict '
    out += 'type= ' + 'int' + ' '

    out += '{'
    for k, v in dd.iteritems():
        encodeType
        out += '\'' + encodeType(k) + '\': '
        out += str(v) + ', '
    return out + '})'

def encode_Alphabet(alpha):
    if alpha is None:
        return '(None)'

    out = '(alphabet '
    out += '_index_to_label= {'

    for key, value in alpha._index_to_label.iteritems():
        # out += str(key) + ': ' + str(value) + ', '
        out += encodeType(key) + ': ' + encodeType(value) + ', '

    out += '} _label_to_index= {'
    for key, value in alpha._label_to_index.iteritems():
        # out += str(key) + ': ' + str(value) + ', '
        out += encodeType(key) + ': ' + encodeType(value) + ', '

    out += '} num_labels= ' + str(alpha.num_labels)
    return out + ')'


def print_Alphabet(alpha):
    if alpha is None:
        return '(None)'

    out = '(alphabet '
    out += '_index_to_label= ' + '{'

    print('_index_to_label')
    for key, value in alpha._index_to_label.iteritems():
        print('key = ' + str(key) + ': ' + str(type(key)))
        print('value = ' + str(value) + ': ' + str(type(value)))

    print('_index_to_label')
    for key, value in alpha._label_to_index.iteritems():
        print('key = ' + str(key) + ': ' + str(type(key)))
        print('value = ' + str(value) + ': ' + str(type(value)))

    print('num_labels = ' + str(alpha.num_labels))

    return out + '})'

def encode_feature_codebook(dd):
    if dd is None:
        return '(None)'

    out = '(dictionary {'
    for key, value in dd.iteritems():
        print('---------------------')
        print('key = ' + str(key) + ': ' + str(type(key)))
        valueEncoded = encode_Alphabet(value)
        out += str(key) + ': ' + str(valueEncoded) + ', '

    return out + '})'
