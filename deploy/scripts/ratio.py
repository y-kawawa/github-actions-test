from typing import List, Optional
from argparse import ArgumentParser


def determine_zone(zones: List[str], rate: int) -> List[str]:
    """
    determine_zone returns a list of zones to be deployed based on the rate
    指定されたrateになるように、zone=1からzoneを選択します
    """
    num = int(len(zones)*rate/100)
    num = 1 if num == 0 else num
    return zones[0:num]


def determine_zone_with_difference(zones: List[str], rate: int, prev_rate: Optional[int]) -> List[str]:
    exclude_zones = []
    if prev_rate:
        # prev_rateが指定された場合はデプロイ済みのzoneを除外する
        exclude_zones = determine_zone(zones, prev_rate)
    candinate_zones = determine_zone(zones, rate)
    return [z for z in candinate_zones if z not in exclude_zones]


def main():
    parse = ArgumentParser()
    parse.add_argument('--rate', type=int, choices=[10, 20, 50, 80, 100], required=True)
    parse.add_argument('--prev-rate', type=int, choices=[10, 20, 50, 80, 100])
    parse.add_argument('--zones', nargs='+', type=str, required=True, help='zone list')
    args = parse.parse_args()

    target_zones = determine_zone_with_difference(args.zones, args.rate, args.prev_rate)
    target_zones_str = ' '.join(target_zones)
    print(target_zones_str)


if __name__ == "__main__":
    main()
