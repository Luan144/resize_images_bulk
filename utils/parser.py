import argparse


parser = argparse.ArgumentParser(description="arguments to resize_bulk")

parser.add_argument("-padding",
                    type=str,
                    default="padding",
                    help="padding to add zero padding.")

parser.add_argument("-x",
                    type=int,
                    default=640,
                    help="enter expected image size.")

parser.add_argument("-y",
                    type=int,
                    default=640,
                    help="enter expected image size.")

parser.add_argument("-prefix",
                    type=str,
                    default="",
                    help="enter a prefix for resized images.")
