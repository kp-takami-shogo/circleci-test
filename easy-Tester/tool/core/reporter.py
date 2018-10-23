# coding:utf-8

import xml.etree.ElementTree as et
from xml.dom import minidom


class Reporter:

    # レポート作成
    def create_report(self, result, report_path=''):
        testsuites = et.Element('testsuites')
        testsuites.set('name', result['testsuites_name'])
        testsuites.set('tests', str(result['testsuites_tests']))
        testsuites.set('failures', str(result['testsuites_failures']))
        testsuites.set('errors', str(result['testsuites_errors']))
        testsuites.set('time', str(round(result['time'], 3)))

        for testsuite_info in result['testsuite_results']:
            testsuite = et.SubElement(testsuites, 'testsuite')
            testsuite.set('name', testsuite_info['testsuite_name'])
            testsuite.set('tests', str(testsuite_info['testsuite_tests']))
            testsuite.set('errors', str(testsuite_info['testsuite_errors']))
            testsuite.set('failures', str(testsuite_info['testsuite_failures']))
            testsuite.set('time', str(round(testsuite_info['time'], 3)))

            for testcase_info in testsuite_info['testcase_results']:
                testcase = et.SubElement(testsuite, 'testcase')
                testcase.set('classname', testsuite_info['testsuite_name'])
                testcase.set('name', testcase_info['testcase_name'])
                testcase.set('time', str(round(testcase_info['time'], 3)))

                if testcase_info['testcase_result'] == 'failure':
                    failure = et.SubElement(testcase, 'failure')
                    failure.set('type', 'AssertionError')
                    failure.set('message', '')
                    failure.text = testcase_info['testcase_content']

                elif testcase_info['testcase_result'] == 'error':
                    error = et.SubElement(testcase, 'error')
                    error.set('type', 'Error')
                    error.set('message', '')
                    error.text = testcase_info['testcase_content']

                elif testcase_info['testcase_result'] == 'skipped':
                    et.SubElement(testcase, 'skipped')

        Reporter.output_report(testsuites, report_path)

    # レポート出力
    @staticmethod
    def output_report(elem, report_path):
        report = minidom.parseString(et.tostring(elem, 'utf-8'))

        file = open(report_path, 'w')
        report.writexml(file, encoding='utf-8', newl='\n', indent='', addindent='  ')
        file.close()

    # XMLを整形（標準出力用）
    @staticmethod
    def prettify(elem):
        rough_string = et.tostring(elem, 'utf-8')
        reparsed = minidom.parseString(rough_string)
        return reparsed.toprettyxml(indent="  ")
