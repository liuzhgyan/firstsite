from urllib import quote, quote_plus, _is_unicode
def urlencode(obj_data, result, p_index = None):
    if not isinstance(obj_data, dict) and p_index is None:
        return None
    # deal list type
    if isinstance(obj_data, list):
        for inner_v in obj_data:
            index_key = p_index
            if isinstance(inner_v, dict):
                # recursively call
                urlencode(inner_v, result, index_key)
            elif isinstance(inner_v, list):
                # recursively call
                urlencode(inner_v, result, '%s[]' % index_key)
            else:
                if _is_unicode(inner_v):
                    inner_v = inner_v.encode("ASCII","replace")
                result.append({p_index:inner_v})
    # deal dict type
    elif isinstance(obj_data, dict):
        for key, value in obj_data.items():
            if p_index is None:
                index_key = key
            else:
                index_key = '%s[%s]' %(p_index, key)
            if isinstance(value, dict):
                # recursively call
                urlencode(value, result, index_key)
            elif isinstance(value, list):
                # recursively call
                urlencode(value, result, '%s[]' % index_key)
            else:
                # deal string similarly value
                # encode transfer
                if _is_unicode(value):
                    value = value.encode("ASCII","replace")
                result.append({index_key:value})
# call example
def gen_urlformat_data(obj_data):
    """
    format data to url string
    :obj_data dict type
    """
    result = list()
    urlencode(obj_data, result)
    print result
    url_elm = list()
    for one_elm in result:
        for key, value in one_elm.items():
            encode_elm = '%s=%s' % (quote_plus(key), quote_plus(str(value)))
            url_elm.append(encode_elm)
    return '&'.join(url_elm)

if __name__ == '__main__':
    data = {'expire_seconds': 1800, 'action_info': {'scene': {'scene_id': 123}}, 'action_name': 'QR_SCENE'}
    print gen_urlformat_data(data)
                