from argparse import ArgumentParser

from openaiclient import MyOpenAI


def run() -> dict[str, str | int | float]:
    """
        Run the application
    """
    parser = ArgumentParser(
                description="Welcome to your travel guide!",
                prog="ULTRA TRAVEL GUIDER 2000",
            )

    # Adding commands 
    parser.add_argument(
        '-d',
        '--destination',
        type=str,
        help="choose your destination",
        required=True,
    )

    parser.add_argument(
        "-o",
        "--origin",
        type=str,
        help="Your origin point, the country or place you are currently in",
        required=True,
    )

    parser.add_argument(
        '-sd',
        '--start_date',
        type=str,
        help="choose the start date of your travel",
        required=True,
    )

    parser.add_argument(
        '-ed',
        '--end_date',
        type=str,
        help='choose the end date of your travel ',
        required=True,
    )

    parser.add_argument(
        '-b',
        '--budget',
        type=float,
        help="Your budget for traveling (in USD)",
        required=True,
    )

    parser.add_argument(
        '-i',
        '--interest',
        help="Places of interest that you want to visit example:'museums, parks'",
        required=False,
        nargs="?",
        default=None,
    )

    parser.add_argument(
        '-cn',
        '--custom_note',
        help="Share anything you want to inform the AI \n" \
        "example: 'I am traveling with my family, suggest family-friendly places'",
        type=str,
        required=False,
        default=None,
    )

    parser.add_argument(
        "-t",
        "--travelers",
        help="How many people that will travel",
        type=int,
        required=False,
        default=1,
    )

    args = parser.parse_args()

    return args


# Testing
if __name__ == '__main__':
    args = run()
    client = MyOpenAI()

    # hardcoded, but this is the way
    all_user_input = [
        args.origin,  
        args.destination,
        args.start_date,
        args.end_date,
        args.budget,
        args.travelers,
        args.interest,
        args.custom_note
    ]

    user_response = client.get_ai_response(all_user_input)

    print(user_response)