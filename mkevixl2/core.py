import click

# from excel_handler import make_file
from mkevixl2.excel_handler import make_file

# from excel_handler import make_file


@click.command()
@click.option("--filename", "-f", default="newfile", show_default=True, help="ファイル名称")
@click.argument("sheetnames", nargs=-1)
def cli(filename, sheetnames):

    # # エビデンス用Excelファイル生成ツール
    if mkevixl2(filename, sheetnames) == False:
        return print("処理失敗")
    else:
        return print("処理完了")


def mkevixl2(filename, sheetnames):

    if len(sheetnames) < 1:
        return False

    make_file(filename, sheetnames)
    return True
