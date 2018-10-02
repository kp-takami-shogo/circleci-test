import axios from 'axios'

const api = axios.create({
  baseURL: 'http://localhost:9001'
})

export async function getProjectList () {
  let json = ''

  try {
    await api
      .get('project')
      .then((r) => {
        json = r.data
      })
  } catch (e) {
    throw e
  }

  return json
}

export async function getBranchList (project) {
  let json = ''

  const params = {'p': project}

  try {
    await api
      .get('branch', {
        params: params
      })
      .then((r) => {
        json = r.data
      })
  } catch (e) {
    throw e
  }

  return json
}

export async function getTestList (project, branch) {
  let json = ''

  const params = {
    'p': project,
    'b': branch
  }

  try {
    await api
      .get('test', {
        params: params
      })
      .then((r) => {
        json = r.data
      })
  } catch (e) {
    throw e
  }

  return json
}

export async function getTestCaseList (project, branch, test) {
  let json = ''

  const params = {
    'p': project,
    'b': branch,
    't': test
  }

  try {
    await api
      .get('test', {
        params: params
      })
      .then((r) => {
        json = r.data
      })
  } catch (e) {
    throw e
  }

  return json
}
