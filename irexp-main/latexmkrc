# Postcard layout: styles live under tex/
# ensure_path: latexmk >= 4.70 (Overleaf). Also set ENV so BibTeX
# subprocesses inherit BSTINPUTS when ensure_path is not applied.
ensure_path( 'TEXINPUTS', './tex//', '../tex//' );
ensure_path( 'BSTINPUTS', './tex//', '../tex//' );

$ENV{'TEXINPUTS'} = './tex//:../tex//:' . (defined $ENV{'TEXINPUTS'} ? $ENV{'TEXINPUTS'} : '');
$ENV{'BSTINPUTS'} = './tex//:../tex//:' . (defined $ENV{'BSTINPUTS'} ? $ENV{'BSTINPUTS'} : '');
