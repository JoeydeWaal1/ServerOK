import argparse
                #(management, check)
def get_args() -> (bool, bool):
    parser = argparse.ArgumentParser(
                    prog='Server OK cmd tool',
                    description='server ping test',
                    epilog='Text at the bottom of help')
    parser.add_argument('-m', "--management", action='store_true')
    parser.add_argument('-c', '--check', action='store_true')

    args = parser.parse_args()
    
    return (args.management, args.check)