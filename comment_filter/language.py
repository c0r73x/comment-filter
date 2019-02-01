class Lang:
    def __init__(self, line_comment, comment_bookends, nested_comments):
        self.line_comment = line_comment
        self.comment_bookends = comment_bookends
        self.nested_comments = nested_comments
        self.string_literals = ['"', '`', "'"]


c = Lang(
    line_comment='//',
    comment_bookends=[('/*', '*/')],
    nested_comments=False)

haskell = Lang(
    line_comment='--',
    comment_bookends=[('{-', '-}')],
    nested_comments=True)

python = Lang(
    line_comment='#',
    comment_bookends=[('"""', '"""'), ("'''", "'''")],
    nested_comments=False)

ruby = Lang(
    line_comment='#',
    comment_bookends=[("=begin", "=end")],
    nested_comments=False)

lua = Lang(
    line_comment='--',
    comment_bookends=[("--[[", "--]]")],
    nested_comments=False)

perl = Lang(
    line_comment='#',
    comment_bookends=[("=pod", "=cut")],
    nested_comments=False)

java = Lang(
    line_comment='//',
    comment_bookends=[('/*', '*/')],
    nested_comments=True)

vim = Lang(
    line_comment='"',
    comment_bookends=[],
    nested_comments=False)

html = Lang(
    line_comment=None,
    comment_bookends=[('<!--', '-->')],
    nested_comments=True)

extension_to_lang_map = {
    '.m': c,
    '.mm': c,
    '.c': c,
    '.cc': c,
    '.cxx': c,
    '.cpp': c,
    '.h': c,
    '.hpp': c,
    '.hh': c,
    '.S': c,
    '.go': c,
    '.js': c,
    '.ts': c,
    '.jsx': c,
    '.tsx': c,
    '.vue': c,
    '.php': c,
    '.java': java,
    '.hs': haskell,
    '.py': python,
    '.rb': ruby,
    '.lua': lua,
    '.pl': perl,
    '.vim': vim,
    '.xml': html,
    '.html': html,
}
