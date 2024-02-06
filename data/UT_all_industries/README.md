This data set can be generated from a full copy of the data file `../USA_full/2021.annual.singlefile.csv`.  Navigate to this directory in your shell and run these commands:

    command head -n 1 ../USA_full/2021.annual.singlefile.csv > header.csv
    command grep '^"49' ../USA_full/2021.annual.singlefile.csv > dat.csv
    command grep '"0","10"' dat.csv > trimmed.csv
    command cat header.csv trimmed.csv > 2021.annual.singlefile.csv
    command rm header.csv dat.csv trimmed.csv

*Note: In some shells the text tools are defined with _aliases_, which may change their output.  The `command` command temporarily restores the default behavior.*

*Note: You may use your own implementation of `tt.py` if it has been **installed**. See [Installing_Text_Tools.md](../../instructions/Installing_Text_Tools.md) for details.*
