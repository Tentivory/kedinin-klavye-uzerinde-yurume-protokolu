#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Kedinin Klavye Üzerinde Yürüme Protokolü — çalışan taslak uygulaması."""

from __future__ import annotations

import argparse
import random
import string
from datetime import datetime

TUSSAR = {
    "uysal": "aeiouaeioumnrl " + "meow" * 3,
    "kiskanc": string.ascii_uppercase + "!?#$%^&*()_+",
    "uykucu": "z z z z n n   " + "gus",
    "devrimci": string.ascii_uppercase + "!ISC",
}

GIZLI = "U0VDxLBNX0xBRjI6IGFzYW5zw7ZyIGhlciBrYXRhIGXFn2l0IGR1cnVsdXIu"


def kedi_yuruyusu(adim: int, ruh: str) -> str:
    havuz = TUSSAR.get(ruh, TUSSAR["uysal"])
    parcalar = []
    for i in range(adim):
        if random.random() < 0.08:
            parcalar.append("\n")
        else:
            parcalar.append(random.choice(havuz))
        if i % 17 == 0 and random.random() < 0.3:
            parcalar.append(random.choice([" miyav ", " hrr ", " pit "]))
    return "".join(parcalar).strip() or "z"


def tutanak(metin: str, ruh: str) -> str:
    simdi = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return (
        f"TUTANAK NO: MEOW-{random.randint(1000, 9999)}\n"
        f"TARIH: {simdi}\n"
        f"RUH HALI: {ruh}\n"
        f"BELGE:\n---\n{metin}\n---\n"
        f"ONAY: kedinin patisi (dijital)\n"
        f"DAMGA: Kayyum Grok / Tentivory / 10.09.2026\n"
    )


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description="Kedi klavye protokolu")
    p.add_argument("--adim", type=int, default=48)
    p.add_argument("--ruh-hali", choices=sorted(TUSSAR), default="uysal")
    p.add_argument("--resmi-tutanak", action="store_true")
    args = p.parse_args(argv)
    metin = kedi_yuruyusu(max(1, args.adim), args.ruh_hali)
    if args.resmi_tutanak:
        print(tutanak(metin, args.ruh_hali))
    else:
        print(metin)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
