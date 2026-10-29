# Notes:
import sys
import json
from pathlib import Path
from typing import Any

# Add project root to sys.path (find the directory containing db_structs.py)
_root = Path(__file__).resolve().parent
while _root.parent != _root:
    if (_root / "db_structs.py").exists():
        if str(_root) not in sys.path:
            sys.path.append(str(_root))
        break
    _root = _root.parent

from db_structs import (
    Medium,
    Circle,
    Event,
    EventGroup,
    Source,
    ReliabilityTypes,
    OriginTypes,
    Location,
)

RT, OT = ReliabilityTypes, OriginTypes

PATH_HELPER = Path(__file__).parent
PATH_EVENT_GROUP = PATH_HELPER.parent
PATH_MEDIA = PATH_EVENT_GROUP / "media"


def retrieve_circles(event_name: str) -> list[Circle]:
    """Retrieve circles of given event. In the circle file has not been created, execute the creation script first."""
    circles_json_path = PATH_HELPER / event_name / "circles.json"
    if not circles_json_path.exists():
        print(
            f"Circle file for {event_name} not found, running the creation script ..."
        )
        creation_script_path = PATH_HELPER / event_name / "main.py"
        if not creation_script_path.exists():
            raise FileNotFoundError(
                f"Creation script for {event_name} not found at {creation_script_path}"
            )
        # Import main() from the creation script and execute
        import importlib.util

        spec = importlib.util.spec_from_file_location(
            f"{event_name}.main", creation_script_path
        )
        if spec and spec.loader:
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            if hasattr(module, "main"):
                module.main()

        if not circles_json_path.exists():
            raise FileNotFoundError(
                f"Creation script {creation_script_path} failed to create {circles_json_path}"
            )

    with circles_json_path.open("r", encoding="utf-8") as f:
        circles_raw = json.load(f)
    return [Circle.load_from_json(c) for c in circles_raw]


if __name__ == "__main__":
    events: list[Event] = []
    disabled_events: list[int | str] = []

    i = 1  # ==== ab_sokubaikai_sensen1 ====
    if i not in disabled_events:
        event_name = f"ab_sokubaikai_sensen{i}"
        print(f"Processing {event_name} ...")

        media_ = [
            Medium(
                "01_paper.jpg",
                [
                    Source(
                        "https://web.archive.org/web/20261026195552/https://mattari-an.net/angelbeats/1st/",
                        (RT.Reliable, OT.Official),
                    )
                ],
                comments="チラシ絵提供：まさゆ 様（ヤモセブン）",
            ),
            Medium(
                "01_titlelogo.gif",
                [
                    Source(
                        "https://web.archive.org/web/20261026195552/https://mattari-an.net/angelbeats/1st/",
                        (RT.Reliable, OT.Official),
                    )
                ],
            ),
            Medium(
                "01_kannai.pdf",
                [
                    Source(
                        "https://web.archive.org/web/20261026195519/https://mattari-an.net/angelbeats/1st/list.html",
                        (RT.Reliable, OT.Official),
                    )
                ],
            ),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
        ]
        locations = [
            Location(
                coordinates=(35.1590924, 136.9298891),
                address="2 Chome-6-3 Fukiage, Chikusa Ward, Nagoya, Aichi 464-0856, Japan",
                description="名古屋中小企業福祉会館 ６階ホール",
                sources=[
                    Source(
                        "https://web.archive.org/web/20261026195552/https://mattari-an.net/angelbeats/1st/",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
                # comments=None,
                imageUrl="https://lh3.googleusercontent.com/gps-cs-s/AHRPTWkq7ADwtY0_LzlU3mk0DFlmJeNo1bo9bpZ2vqyiopbdHLCB4zA_pSkSpa9YKGQsJgPRhkx6a0R8e8OPBlstCq-5saYTJ5-avtnX6fZR-cI6YHIZgV7pYeOLMsw_PDlSU2wW-9f9=s0?imgmax=0",
                url="https://maps.app.goo.gl/5QerDbUB3hz5Xcjq9",
            ),
        ]
        event = Event(
            aliases=["AB即売会戦線", "AB Sokubaikai Sensen"],
            dates="2010.09.19",
            circles=[],
            media=media_,
            sources=[
                Source(
                    "Date: https://web.archive.org/web/20261026195552/https://mattari-an.net/angelbeats/1st/",
                    (RT.Reliable, OT.Official),
                ),
                Source(
                    "Participating circles: https://web.archive.org/web/20261026195519/https://mattari-an.net/angelbeats/1st/list.html",
                    (RT.Reliable, OT.Official),
                ),
            ],
            locations=locations,
            description="Simultaneous with リトバスパーティー3",
            # comments=None,
            last_edited="2026.10.26",
        )

        # Retrieve circles
        event.circles = retrieve_circles(event_name)
        events.append(event)

    i = 2  # ==== ab_sokubaikai_sensen2 ====
    if i not in disabled_events:
        event_name = f"ab_sokubaikai_sensen{i}"
        print(f"Processing {event_name} ...")

        media_ = [
            Medium(
                "02_paper.jpg",
                [
                    Source(
                        "https://web.archive.org/web/20261029192612/https://mattari-an.net/angelbeats/2nd/",
                        (RT.Reliable, OT.Official),
                    )
                ],
                comments="チラシ絵提供：神楽七姫 様（Navy Blue）",
            ),
            Medium(
                "02_titlelogo.gif",
                [
                    Source(
                        "https://web.archive.org/web/20261029192612/https://mattari-an.net/angelbeats/2nd/",
                        (RT.Reliable, OT.Official),
                    )
                ],
            ),
            Medium(
                "02_kannai.jpg",
                [
                    Source(
                        "https://web.archive.org/web/20261029192740/https://mattari-an.net/angelbeats/2nd/list.html",
                        (RT.Reliable, OT.Official),
                    )
                ],
            ),
            Medium(
                "02_kannai.pdf",
                [
                    Source(
                        "https://web.archive.org/web/20261029192740/https://mattari-an.net/angelbeats/2nd/list.html",
                        (RT.Reliable, OT.Official),
                    )
                ],
            ),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
        ]
        locations = [
            Location(
                coordinates=(35.01365, 135.7809429),
                address="9-1 Okazaki Seishojicho, Sakyo Ward, Kyoto, 606-8343, Japan",
                description="京都市勧業館　みやこめっせ　３階 第３展示場Ａ面",
                sources=[
                    Source(
                        "https://web.archive.org/web/20261025180224/https://mattari-an.net/keyparty/1st/",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
                # comments=None,
                imageUrl="https://lh3.googleusercontent.com/gps-cs-s/AHRPTWlur6oWztq77DaOuTZLw5MRyj3iDVD1CD-wl9_7wkEXC7e9JYhls5YX8XY6_936CE_RWP6CozLolZI73Mh7gleO-PgU9DJro4VpNaq7nQSPaHd9rChZ-VVge7urD47mbsVOMZ6B-A=s870-k-no",
                url="https://maps.app.goo.gl/8MjxYFEFKBxjhyTT8",
            ),
        ]
        event = Event(
            aliases=["AB即売会戦線2", "AB Sokubaikai Sensen 2"],
            dates="2011.03.27",
            circles=[],
            media=media_,
            sources=[
                Source(
                    "Date: https://web.archive.org/web/20261029192612/https://mattari-an.net/angelbeats/2nd/",
                    (RT.Reliable, OT.Official),
                ),
                Source(
                    "Participating circles: https://web.archive.org/web/20261029192740/https://mattari-an.net/angelbeats/2nd/list.html",
                    (RT.Reliable, OT.Official),
                ),
            ],
            locations=locations,
            description="Simultaneous with Keyパーティー and リトバスパーティー4",
            # comments=None,
            last_edited="2026.10.29",
        )

        # Retrieve circles
        event.circles = retrieve_circles(event_name)
        events.append(event)

    i = 3  # ==== ab_sokubaikai_sensen3 ====
    if i not in disabled_events:
        event_name = f"ab_sokubaikai_sensen{i}"
        print(f"Processing {event_name} ...")

        media_ = [
            Medium(
                "03_paper.jpg",
                [
                    Source(
                        "https://web.archive.org/web/20110820184802/http://mattari-an.net/angelbeats/",
                        (RT.Reliable, OT.Official),
                    )
                ],
                comments="チラシ絵提供：猫足とろろ 様（とろろのお宿）",
            ),
            Medium(
                "03_titlelogo.gif",
                [
                    Source(
                        "https://web.archive.org/web/20110820184802/http://mattari-an.net/angelbeats/",
                        (RT.Reliable, OT.Official),
                    )
                ],
            ),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
        ]
        locations = [
            Location(
                coordinates=(35.1708859, 136.8837218),
                address="4-chōme-4-38 Meieki, Nakamura Ward, Nagoya, Aichi 450-0002, Japan",
                description="愛知県産業労働センター（ウインクあいち）　６階展示場",
                sources=[
                    Source(
                        "https://web.archive.org/web/20110820184802/http://mattari-an.net/angelbeats/",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
                # comments=None,
                imageUrl="https://streetviewpixels-pa.googleapis.com/v1/thumbnail?output=thumbnail&cb_client=maps_sv.tactile.gps&panoid=plEI7dd2WTUE58egOJKX3g&w=1177&h=1300&yaw=170&pitch=-40",
                url="https://maps.app.goo.gl/6F2N7Dtys66bRMQQ9",
            ),
        ]
        event = Event(
            aliases=["AB即売会戦線3", "AB Sokubaikai Sensen 3"],
            dates="2011.09.11",
            circles=[],
            media=media_,
            sources=[
                Source(
                    "Date: https://web.archive.org/web/20110820184802/http://mattari-an.net/angelbeats/",
                    (RT.Reliable, OT.Official),
                ),
                Source(
                    "Participating circles: https://web.archive.org/web/20110918034246/http://mattari-an.net/angelbeats/list.html",
                    (RT.Reliable, OT.Official),
                ),
            ],
            locations=locations,
            description="Simultaneous with Keyパーティー2",
            # comments=None,
            last_edited="2026.10.29",
        )

        # Retrieve circles
        event.circles = retrieve_circles(event_name)
        events.append(event)

    i = 4  # ==== ab_sokubaikai_sensen4 ====
    if i not in disabled_events:
        event_name = f"ab_sokubaikai_sensen{i}"
        print(f"Processing {event_name} ...")

        media_ = [
            Medium(
                "04_paper.jpg",
                [
                    Source(
                        "https://web.archive.org/web/20261025180308/http://mattari-an.net/angelbeats/",
                        (RT.Reliable, OT.Official),
                    )
                ],
                comments="表紙絵提供：ふゆいち 様（Pendola）",
            ),
            Medium(
                "04_titlelogo.gif",
                [
                    Source(
                        "https://web.archive.org/web/20261025180308/http://mattari-an.net/angelbeats/",
                        (RT.Reliable, OT.Official),
                    )
                ],
            ),
            Medium(
                "04_kannai.pdf",
                [
                    Source(
                        "https://web.archive.org/web/20250324061852/https://mattari-an.net/angelbeats/list.html",
                        (RT.Reliable, OT.Official),
                    )
                ],
            ),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
        ]
        locations = [
            Location(
                coordinates=(35.1590924, 136.9298891),
                address="2 Chome-6-3 Fukiage, Chikusa Ward, Nagoya, Aichi 464-0856, Japan",
                description="名古屋中小企業福祉会館　６階ホール",
                sources=[
                    Source(
                        "https://web.archive.org/web/20261025180308/http://mattari-an.net/angelbeats/",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
                # comments=None,
                imageUrl="https://lh3.googleusercontent.com/gps-cs-s/AHRPTWkq7ADwtY0_LzlU3mk0DFlmJeNo1bo9bpZ2vqyiopbdHLCB4zA_pSkSpa9YKGQsJgPRhkx6a0R8e8OPBlstCq-5saYTJ5-avtnX6fZR-cI6YHIZgV7pYeOLMsw_PDlSU2wW-9f9=s0?imgmax=0",
                url="https://maps.app.goo.gl/5QerDbUB3hz5Xcjq9",
            ),
        ]
        event = Event(
            aliases=["AB即売会戦線4", "AB Sokubaikai Sensen 4"],
            dates="2012.09.16",
            circles=[],
            media=media_,
            sources=[
                Source(
                    "Date: https://web.archive.org/web/20261025180308/http://mattari-an.net/angelbeats/",
                    (RT.Reliable, OT.Official),
                ),
                Source(
                    "Participating circles: https://web.archive.org/web/20250324061852/https://mattari-an.net/angelbeats/list.html",
                    (RT.Reliable, OT.Official),
                ),
            ],
            locations=locations,
            description="Simultaneous with Keyパーティー3",
            # comments=None,
            last_edited="2026.10.29",
        )

        # Retrieve circles
        event.circles = retrieve_circles(event_name)
        events.append(event)

    # i =   # ==== ab_sokubaikai_sensen ====
    # if i not in disabled_events:
    #     event_name = f"ab_sokubaikai_sensen{i}"
    #     print(f"Processing {event_name} ...")

    #     media_ = [
    #         # Medium("", [Source("", (RT.Reliable, OT.Official))]),
    #         # Medium("", [Source("", (RT.Reliable, OT.Official))]),
    #         # Medium("", [Source("", (RT.Reliable, OT.Official))]),
    #     ]
    #     locations = [
    #         # Location(
    #         #     coordinates=(,),
    #         #     address="",
    #         #     description="",
    #         #     sources=[Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))],
    #         #     # comments=None,
    #         #     imageUrl="",
    #         #     url="",
    #         # ),
    #     ]
    #     event = Event(
    #         # aliases=["AB即売会戦線", "AB Sokubaikai Sensen"],
    #         # dates="",
    #         circles=[],
    #         media=media_,
    #         sources=[
    #             # Source("Date: ", (RT.Reliable, OT.Official)),
    #             # Source("Participating circles: ", (RT.Reliable, OT.Official)),
    #         ],
    #         locations=locations,
    #         description=None,
    #         # comments=None,
    #         last_edited="2026.10.29",
    #     )

    #     # Retrieve circles
    #     # event.circles = retrieve_circles(event_name)
    #     events.append(event)

    # ==== event group ====
    media = [
        # Medium("",
        #        [Source("", (RT.Reliable, OT.Official))]),
        # Medium("",
        #        [Source("", (RT.Reliable, OT.Official))]),
    ]
    links = ["http://mattari-an.net/angelbeats/", "http://twitter.com/key_party_abss"]

    event_group = EventGroup(
        aliases=[
            "AB即売会戦線",
            "AB Sokubaikai Sensen",
            "Angel Beats! 即売会戦線",
            "Angel Beats! Sokubaikai Sensen",
        ],
        events=events,
        media=media,
        links=links,
        sources=[
            Source(
                "Alias transliteration: guessed from onyomi", (RT.Guess, OT.Unsourced)
            ),
        ],
        comments=None,
        description=None,
        last_edited="2026.10.29",
    )

    print(f"Saving {Path(__file__).stem} database...")
    event_group.save(PATH_EVENT_GROUP, indent=None)
    print("Done")
