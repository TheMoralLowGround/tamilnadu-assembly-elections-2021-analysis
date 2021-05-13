import scrapy
import pandas as pd


class EciSpider(scrapy.Spider):
    name = "eci"
    allowed_domains = ["results.eci.gov.in/"]
    # start_urls = ["https://results.eci.gov.in//"]

    # https://results.eci.gov.in/Result2021/ConstituencywiseS2228.htm?ac=28
    # https://results.eci.gov.in/Result2021/ConstituencywiseS22182.htm?ac=182
    # https://results.eci.gov.in/Result2021/ConstituencywiseS22223.htm?ac=223

    def start_requests(self):
        for i in range(1, 235):
            url = f"https://results.eci.gov.in/Result2021/ConstituencywiseS22{i}.htm?ac={i}"
            yield scrapy.Request(url=url, callback=self.parse)
            # return  # temporary

    def parse(self, response):
        rows = response.xpath(
            '//*[@id="div1"]/table[1]/tbody/tr'
        ).getall()  # response is a list
        rows = (
            "<table>" + "".join(rows[2:-1]) + "</table>"
        )  # join converts list to str, appending table tag
        table = pd.read_html(rows)[0]
        ac_no = response.url.split("ac=")[-1]
        # print(table)
        table.to_csv(f"{ac_no}.csv", index=False)
        print("Saved Constituency", ac_no)
