from utils.parser import parse_args
from core import predict_from_files


def LinkSeg():
    args = parse_args()
    predict_from_files(**vars(args))


if __name__ == "__main__":
    LinkSeg()