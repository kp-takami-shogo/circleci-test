#!/usr/bin/env bash

cd `dirname $0`

test_dir=./../eT-test
testcase_dir=./../eT-test/testcase
reports_dir=./../eT-test/reports
artifacts_dir=./../eT-test/artifacts

create_dir_flg=0

if [ ! -e ${test_dir} ]; then
    mkdir ${test_dir}

    if [ $? -eq 0 ]; then
        create_dir_flg=1
    else
        create_dir_flg=2
    fi
fi

if [ ! -e ${testcase_dir} ]; then
    mkdir ${testcase_dir}

    if [ $? -eq 0 ]; then
        create_dir_flg=1
    else
        create_dir_flg=2
    fi
fi

if [ ! -e ${reports_dir} ];then
    mkdir ${reports_dir}

    if [ $? -eq 0 ]; then
        create_dir_flg=1
    else
        create_dir_flg=2
    fi
fi

if [ ! -e ${artifacts_dir} ];then
    mkdir ${artifacts_dir}

    if [ $? -eq 0 ]; then
        create_dir_flg=1
    else
        create_dir_flg=2
    fi
fi

if [ ${create_dir_flg} -eq 1 ]; then
    echo "I have created a eT-test directory."
    echo ""
elif [ ${create_dir_flg} -eq 2 ]; then
    echo "\033[31mFailed to create eT-test directory.\033[0m"
    echo ""
fi

echo "Set up Python."
pip install selenium==3.8.0 pyyaml

if [ $? -ne 0 ]; then
    echo "\033[31mFailed to set up Python.\033[0m"
fi

echo ""

echo "Set up cli."
pip install -e ./cli/

if [ $? -ne 0 ]; then
    echo "\033[31mFailed to set up cli.\033[0m"
fi
