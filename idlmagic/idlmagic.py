"""
IDL cell and line magics for IPython / Jupyter.
"""


from IPython.core.magic import Magics, magics_class, line_magic, cell_magic


def load_ipython_extension(ipython):
    ipython.register_magics(IDLMagics)


@magics_class
class IDLMagics(Magics):

    @line_magic("idl")
    def idl_line_magic(self, line):
        idl_run(line)

    @cell_magic("idl")
    def idl_cell_magic(self, line, cell):
        try:
            sigil_start, sigil_end = line.split()
        except Exception:
            sigil1, sigil2 = "<<", ">>"

        cell = (cell.replace("{", "{{").replace("}", "}}")
                    .replace(sigil1, "{").replace(sigil2, "}"))
        cell = cell.format(**globals())

        idl_run(cell)

    @line_magic("idl_var")
    def idl_var(self, line):
        return idl_get_var(line.strip())


def idl_run(commands, r=None):
    """
    Run one or multiple commands in IDL using the ``idlpy`` bridge.

    Parameters
    ----------
    commands : string
        The IDL command(s) to run. Multiple lines are supported.
    r : string or None, optional
        Name of an IDL variable whose value is returned by this function.

    Returns
    -------
    idl_return_value : object or None
        Only returned if `r` was provided. This is the value of the IDL
        variable specified by `r`.

    """

    import idlpy

    lines = commands.strip().splitlines()

    # remove comments (required before merging into single line)
    for i, line in enumerate(lines):
        line = line.split(";", maxsplit=1)[0]
        lines[i] = line

    # remove empty lines
    lines = [line for line in lines if line.strip() != ""]

    # handle line continuation `$`
    merge = []  # indices of the lines which should be merged with their prev.
    for i, line in enumerate(lines):
        if line.endswith("$"):
            merge.append(i + 1)

    for m in merge[::-1]:
        lines[m - 1] = lines[m - 1][:-1] + lines[m]
        del lines[m]

    # merge lines
    single_line = " & ".join(lines)

    try:
        res = idlpy.IDL.run(single_line)
    except idlpy.IDLError as e:
        print("\033[31mIDLError:\033[0m")
        print(e)
        return None

    if res is not None:
        print(res)

    # return `r` variable
    if r is not None:
        return idl_get_var(r)


def idl_get_var(r):
    import idlpy
    return getattr(idlpy.IDL, r)
