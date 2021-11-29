import asyncio
import pyppeteer
import time

CANDIDATE_INDEX = 0
FILE_NAME = 'registry.txt'

async def main():
    browser = await pyppeteer.launch(defaultViewport={'width': 1920, 'height': 1080}, headless=False)

    page = await browser.newPage()

    await page.goto('https://afazenda.r7.com/a-fazenda-13/votacao')
    while True:
        time.sleep(0.5)
        candidates = await page.querySelectorAll('.voting-card')
        if(CANDIDATE_INDEX < len(candidates)):
            candidate = candidates[CANDIDATE_INDEX]
            await candidate.click()
            time.sleep(0.5)
            iframes = await page.querySelectorAll('iframe')
            for iframe in iframes:
                prop = await iframe.getProperty('src')
                prop = await prop.jsonValue()
                if 'hcaptcha-checkbox' in prop:
                    await iframe.click()
                    time.sleep(1.0)
                    button = await page.querySelector('.voting-button')
                    await button.click()
                    time.sleep(1.0)
                    confirmation = await page.querySelector('.vote-confirmation__text')
                    with open(FILE_NAME, 'a') as f:
                        if confirmation != None:
                            f.write('1')
                        else:
                            f.write('0')
        else:
            print('Invalid candidate index.')   
            exit(1) 
        await page.reload()

    await page.close()

    await browser.close()

asyncio.get_event_loop().run_until_complete(main())