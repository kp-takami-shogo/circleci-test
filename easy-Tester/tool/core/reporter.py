# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET
from xml.dom import minidom

class Reporter:

    # レポート作成
    def createReport(self, result, *, report_path = 'result.xml'):
        testsuites = ET.Element('testsuites')

        for testsuite_info in result:
            testsuite = ET.SubElement(testsuites, 'testsuite')
            testsuite.set('name', testsuite_info['testsuite_name'])
            testsuite.set('tests', str(testsuite_info['testsuite_tests']))
            testsuite.set('errors', str(testsuite_info['testsuite_errors']))
            testsuite.set('failures', str(testsuite_info['testsuite_failures']))

            for testcase_info in testsuite_info['testcase_results']:
                testcase = ET.SubElement(testsuite, 'testcase')
                testcase.set('classname', testsuite_info['testsuite_name'])
                testcase.set('name', testcase_info['testcase_name'])

                if testcase_info['testcase_result'] == 'failure':
                    failure = ET.SubElement(testcase, 'failure')
                    failure.set('type', 'AssertionError')
                    failure.set('message', '')
                    failure.text = testcase_info['testcase_content']

                elif testcase_info['testcase_result'] == 'error':
                    error = ET.SubElement(testcase, 'error')
                    error.set('type', 'Error')
                    error.set('message', '')
                    error.text = testcase_info['testcase_content']

                elif testcase_info['testcase_result'] == 'skipped':
                    skipped = ET.SubElement(testcase, 'skipped')

        self.outputReport(testsuites, report_path)


    # レポート出力
    def outputReport(self, elem, report_path = 'result.xml'):
        report = minidom.parseString(ET.tostring(elem, 'utf-8'))

        file = open(report_path, 'w')
        report.writexml(file, encoding='utf-8', newl='\n', indent='', addindent='  ')
        file.close()


    # XMLを整形（標準出力用）
    def prettify(self, elem):
        rough_string = ET.tostring(elem, 'utf-8')
        reparsed = minidom.parseString(rough_string)
        return reparsed.toprettyxml(indent="  ")
