import logging
logger = logging.getLogger(f"{__name__}.Report")

import pandas as pd

class Report:
    
    @staticmethod
    def get_data_and_return(page):
        try:
            page.evaluate("""
            () => {
                const elements = document.querySelectorAll("tr[data-id]");
                elements.forEach((el, index) => {
                    el.id = "inconsistency-" + (index + 1);
                });
            }
            """)

            page.wait_for_load_state('load')

            data = page.evaluate("""
            () => {
                const data = [];
                    for (let i = 1; i <= 99; i++) {
                        const row = document.querySelector('#inconsistency-' + i);
                        if (row) {
                            data.push({
                                index: i,
                                name: row.querySelector('td.ng-binding:nth-child(2)').textContent,
                                hour: row.querySelector('td.ng-binding:nth-child(6)').textContent,
                                category: row.querySelector('td.ng-binding:nth-child(7)').textContent,
                            });
                        }
                    }
                return data;
            }
            """)

            page.wait_for_load_state('load')
            
            return data
        except Exception as e:
            logger.error(f"An error occurred while trying to get data in report: {e}")
    
    def _format_data():
        pass
    
    @staticmethod
    def generate_report(data, path):
        for item in data:
            print(item)
        pass
    
    
    

    
    