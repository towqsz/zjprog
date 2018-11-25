from Lab2 import GildedRose, Item

import unittest
import logging
import sys
import copy

itms=[]
itms2=itms
items=["Aged Brie", "Backstage passes to a TAFKAL80ETC concert",
       "Sulfuras, Hand of Ragnaros", "Item1", "Item2", "Item3", "Conjured"]


def new_item(sell_in=10, val=10):
    for item in items:
        itms.append(Item(item, sell_in, val))

def remove_unwanted_items(it_list=["Aged Brie", "Backstage passes to a TAFKAL80ETC concert",
       "Sulfuras, Hand of Ragnaros", "Conjured"]):
    val=itms2[0].quality
    sell_in=itms2[0].sell_in
    itms_l=items.copy()
    itms=[]
    for it in it_list:
        itms_l.remove(it)
    for item in itms_l:
        itms.append(Item(item, sell_in, val))
    return itms
    
    
class KataTest(unittest.TestCase):
    

    def test_item_value(self):
        log= logging.getLogger( "KataTest.test_item_value" )
        log.debug('''\n\n\n\
            ____________________________
            Running: test_item_value
            ____________________________''')
        new_item()
        for _ in range(100):
            GildedRose(itms).update_quality()

        for item in itms:
            self.assertTrue(item.quality>=0)
            self.assertFalse(item.quality>50)
            log.debug("\nValue of {}: {}".format(item.name, item.quality))
        log.debug("\n\nTest passed!\n\n")            

    def test_brie_value(self):
        log= logging.getLogger(
            "KataTest.test_brie_value" )
        log.debug('''\n\n\n\
            ____________________________
            Running: test_brie_value
            ____________________________''')
        brie=Item("Aged Brie", 10, 10)
        prv_quality = brie.quality
        for _ in range(100):
            GildedRose([brie]).update_quality()
            self.assertTrue(brie.quality>=prv_quality)
            quality_diff = brie.quality - prv_quality
            if brie.quality < 50:
                self.assertTrue(
                    quality_diff==1 if brie.sell_in >= 0 else quality_diff==2)
                log.debug("Brie value: {}".format(brie.quality))
            prv_quality = brie.quality
        log.debug("\n\nTest passed!\n\n")

    def test_sulfuras_value(self):
        log= logging.getLogger(
            "KataTest.test_sulfuras_value" )
        log.debug('''\n\n\n\
            ____________________________
            Running: test_sulfuras_value
            ____________________________''')
        sulf=Item("Sulfuras, Hand of Ragnaros", 10, 10)
        prv_quality = sulf.quality
        prv_sell_in = sulf.sell_in
        for _ in range(100):
            GildedRose([sulf]).update_quality()
            self.assertTrue(sulf.quality==prv_quality and sulf.sell_in == prv_sell_in)
            prv_quality = sulf.quality
            prv_sell_in = sulf.sell_in

        log.debug("\n\nTest passed!\n\n")
        
    def test_item_value_decrease(self):
        log= logging.getLogger( "KataTest.test_item_value_decrease" )
        log.debug('''\n\n\n\
            ____________________________
            Running: test_item_value_decrease
            ____________________________''')
        new_item(25, 50)
        itms = remove_unwanted_items()
        log.debug(itms)

        while itms[0].quality>0:
            prv_itms=copy.deepcopy(itms)
            
            GildedRose(itms).update_quality()
            for i, item in enumerate(itms):
                quality_diff = prv_itms[i].quality - item.quality
                log.debug("i: {}\n"
                          "Prv: {} \n Actual: {}".format(i, prv_itms[i].quality, item.quality))
                self.assertTrue(
                    quality_diff==1 if (item.sell_in >= 0 or prv_itms[i].quality==1)
                    else quality_diff==2)

    def test_conjured_value_decrease(self):
        log= logging.getLogger( "KataTest.test_conjured_value_decrease" )
        log.debug('''\n\n\n\
            ____________________________
            Running: test_conjured_value_decrease
            ____________________________''')
        new_item(25, 50)
        to_remove = []
        for item in items:
            if item != "Conjured":
                to_remove.append(item)
        itms = remove_unwanted_items(to_remove)
        log.debug(itms)

        while itms[0].quality>0:
            prv_itms=copy.deepcopy(itms)
            
            GildedRose(itms).update_quality()
            for i, item in enumerate(itms):
                quality_diff = prv_itms[i].quality - item.quality
                log.debug("i: {}\n"
                          "Prv: {} \n Actual: {}".format(i, prv_itms[i].quality, item.quality))
                self.assertTrue(
                    quality_diff==2 if (prv_itms[i].sell_in>0)
                    else quality_diff==4)


        log.debug("\n\nTest passed!\n\n")


if __name__ == '__main__':
    logging.basicConfig( stream=sys.stderr )
    logging.getLogger( "KataTest.test_item_value" ).setLevel( logging.DEBUG )
    logging.getLogger( "KataTest.test_brie_value" ).setLevel( logging.DEBUG )
    logging.getLogger( "KataTest.test_sulfuras_value" ).setLevel( logging.DEBUG )
    logging.getLogger( "KataTest.test_item_value_decrease" ).setLevel( logging.DEBUG )
    logging.getLogger( "KataTest.test_conjured_value_decrease" ).setLevel( logging.DEBUG )
    unittest.main()

