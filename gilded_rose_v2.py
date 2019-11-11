# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):


        
        for item in self.items:
            if item.name == "Sulfuras, Hand of Ragnaros":
                continue
            elif item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
                if item.quality > 0:
                    item.quality = item.quality - 1
                if item.name == "Conjured Mana Cake" and item.quality > 0:
                    item.quality = item.quality - 1
            else:
                if item.name != "Conjured Mana Cake":
                    item.quality = item.quality + 1
                    if item.name == "Backstage passes to a TAFKAL80ETC concert":
                        if item.sell_in < 11:
                            item.quality = item.quality + 1
                        if item.sell_in < 6:
                            item.quality = item.quality + 1
            item.sell_in = item.sell_in - 1
            if item.sell_in < 0:
                if item.name != "Aged Brie":
                    if item.name != "Backstage passes to a TAFKAL80ETC concert":
                        if item.quality > 0:
                            if item.name != "Conjured Mana Cake":
                                item.quality = item.quality - 1
                            elif item.name == "Conjured Mana Cake" and item.quality > 1:
                                item.quality = item.quality - 2
                            elif item.name == "Conjured Mana Cake" and item.quality < 2:
                                item.quality = 0
                    else:
                        item.quality = item.quality - item.quality
                else:
                    item.quality = item.quality + 1
            if item.quality > 50:
                item.quality = 50           



class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)