from pathlib import Path
import difflib
p1=Path(r'd:\github\ENEL445\report\20260503 REPORT.tex')
p2=Path(r'd:\github\ENEL445\report\20260504 REPORT.tex')
out=Path(r'd:\github\ENEL445\report\20260504A REPORT.tex')
if not p1.exists():
    print('MISSING', p1)
    raise SystemExit(2)
if not p2.exists():
    print('MISSING', p2)
    raise SystemExit(2)
text1=p1.read_text(encoding='utf-8')
text2=p2.read_text(encoding='utf-8')
lines1=text1.splitlines(keepends=True)
lines2=text2.splitlines(keepends=True)
ud=''.join(difflib.unified_diff(lines1, lines2, fromfile='report/20260503 REPORT.tex', tofile='report/20260504 REPORT.tex'))
out.write_text(ud, encoding='utf-8')
print('WROTE', out, 'bytes=', len(ud))