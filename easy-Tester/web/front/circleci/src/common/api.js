import axios from 'axios'

const api = axios.create({
  baseURL: 'http://localhost:5042'
})

export async function getTestCaseList () {
  let json = ''

  try {
    await api
      .get('testcase/list')
      .then((r) => {
        json = r.data
      })
  } catch (e) {
    throw e
  }

  return json
}

export async function getTestCase (testcaseName) {
  let json = ''

  try {
    await api
      .get(`testcase/get/${testcaseName}`)
      .then((r) => {
        json = r.data
      })
  } catch (e) {
    throw e
  }

  return json
}
