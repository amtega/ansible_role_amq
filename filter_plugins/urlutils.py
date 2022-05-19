"""Filters: urlsplit_splitquery, urlcombine.

Filters:
    urlsplit_splitquery: given the dictionary returned by the urlsplit filter
                         parses the query key into a dictionary.
    urlcombine: Composes a URL from a dictionary using the same keys as
                produced by the urlsplit filter.
"""

from __future__ import absolute_import, division, print_function
from ansible.module_utils.six.moves.urllib.parse import parse_qs

__metaclass__ = type

ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}


def amq_parse_url_amq_query_string(query_str):
    """Return a dict of the parsed elements of a URL query string component

    Args:
        query_str(str): URL query string component

    Returns:
        dict: dict of the parsed elements of a URL query string component
    """
    return dict(
        (k, v if len(v) > 1 else v[0]) for k, v in parse_qs(query_str).items()
    )


def amq_query_string(query_dict):
    """Return the URL query string representation of a dictionary

    Args:
        query_dict(dict): Parameters for a URL query

    Returns:
        str: URL query string representation of a dictionary
    """
    return ";".join("%s=%s" % (key, val) for (key, val) in query_dict.items())


def amq_urlsplit_split_query(urlsplit_value):
    """Convert query key to dictionary.

    Given the dictionary returned by the urlsplit filter parses the query key
    into a dictionary

    Args:
        urlsplit_value(dict): Dictionary returned by the urlsplit filter.

    Returns:
        dict: dict of the parsed elements of a URL query
    """
    urlsplit_value["query"] = \
        amq_parse_url_amq_query_string(urlsplit_value["query"])

    return urlsplit_value


def amq_url_combine(split_url):
    """Composes a URL from a dictionary.

    From a dictionary using the same keys as produced by the urlsplit filter
    composes a URL.

    Args:
        split_url(dict): dictionary using the same keys as produced by the
            urlsplit filter

    Returns:
        str: URL constructed from split_url
    """
    result = ""

    if split_url["scheme"]:
        result = "{}:".format(split_url["scheme"])
    if split_url["hostname"]:
        result = "{}//{}".format(result, split_url["hostname"])
    if split_url["port"]:
        result = "{}:{}".format(result, split_url["port"])
    if split_url["path"]:
        result = "{}{}".format(result, split_url["path"])
    if split_url["query"]:
        if type(split_url["query"]) is dict:
            result = "{}?{}".format(result,
                                    amq_query_string(split_url["query"]))
        else:
            result = "{}?{}".format(result, split_url["query"])
    if split_url["fragment"]:
        result = "{}#{}".format(result, split_url["fragment"])

    return result


def merge_java_parameters(old, new):
    """Allows adding/replacing parameters in artemis.profile JAVA_ARGS

    Merges the new given parameters into a JAVA_ARGS config value from an
    artemis.profile file.

    Args:
        old(string): Line containing JAVA_ARGS config value from an
            artemis.profile file.

        new(list): List containing the parameters to merge in the JAVA_ARGS
            config value from an artemis.profile file. List format:
            * value: value of the parameter. When undefined, parameter will be
                deleted.
            * param: Name of the parameter, containing all the characters non
                included in 'value'.
            Example:
                [{'param': '-Dhawtio.role='},
                 {'param': '-Dhawtio.roles=', 'value': 'admin,user'}]

    Returns:
        str: Merged JAVA_ARGS config value ready to insert into a
            artemis.profile file.
    """
    result = old.strip()

    if result.startswith('JAVA_ARGS='):
        with_declaration = True
        result = result.replace('JAVA_ARGS=', '', 1)
    else:
        with_declaration = False

    if result and result[0] == result[-1] == '"':
        quoted = True
        result = result[1:-1]
    else:
        quoted = False

    for argument in sorted(new, key=lambda argument: argument['param']):
        param = argument['param']
        if 'value' in argument.keys():
            new_argument = param + argument['value']
        else:
            new_argument = ""  # Delete argument
        if param in result:
            if not new_argument or new_argument not in result:
                position_ini = result.find(param)
                position_end = result.find(' ', position_ini)
                result = (
                    result[:position_ini]
                    + new_argument
                    + result[position_end:]
                )
        else:
            result += " " + new_argument

        result = result.strip()

    if quoted:
        result = '"{}"'.format(result)
    if with_declaration:
        result = 'JAVA_ARGS={}'.format(result)
    return result


class FilterModule(object):
    def filters(self):
        return {"urlsplit_splitquery": amq_urlsplit_split_query,
                "urlcombine": amq_url_combine,
                "merge_java_parameters": merge_java_parameters,
                }
