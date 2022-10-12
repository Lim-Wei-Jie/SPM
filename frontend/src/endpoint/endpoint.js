import axios from "axios";

// Get all Job Roles
export function getAllRoles() {
    return new Promise((resolve, reject) => {
        let apiEndpoint = `${import.meta.env.VITE_APP_DEV_API_ENDPOINT}/role`
        axios
            .get(apiEndpoint)
            .then((res) => {
                resolve(res.data.data.Role)
            })
            .catch((err) => {
                console.log(err);
                reject('Fail to fetch all job roles, check WAMP/MAMP server')
            })
    })
}

// Get specific Job role using Job Role ID / Name
export function getRoleDetails(jobRoleName) {
    return new Promise((resolve, reject) => {
        let apiEndpoint = `${import.meta.env.VITE_APP_DEV_API_ENDPOINT}/role/name/${jobRoleName}`
        axios
            .get(apiEndpoint)
            .then((res) => {
                resolve(res.data.data.Role[0])
            })
            .catch((err) => {
                console.log(err);
                reject('Fail to fetch all job roles, check WAMP/MAMP server')
            })
    })
}

// Get all skills using Job Role ID / Name
export function getSkillsByRole(jobRoleID) {
    console.log(jobRoleID);
    // return new Promise((resolve, reject) => {
    //     let apiEndpoint = `${import.meta.env.VITE_APP_DEV_API_ENDPOINT}/role/getskill/${jobRoleID}`
    //     axios
    //         .get(apiEndpoint)
    //         .then((res) => {
    //             resolve(res.data)
    //         })
    //         .catch((err) => {
    //             console.log(err);
    //             reject('Fail to fetch all skills, check WAMP/MAMP server')
    //         })
    // })
}

// Get specific courses using skill ID / Name
export function getCourses(skillID) {
    return new Promise((resolve, reject) => {
        let apiEndpoint = `${import.meta.env.VITE_APP_DEV_API_ENDPOINT}/role/getcourse/${skillID}`
        axios
            .get(apiEndpoint)
            .then((res) => {
                resolve(res.data)
            })
            .catch((err) => {
                console.log(err);
                reject('Fail to fetch all courses, check WAMP/MAMP server')
            })
    })
}

// Create job role
export function createRole(newJobRoleData) {
    return new Promise((resolve, reject) => {
        let apiEndpoint = `${import.meta.env.VITE_APP_DEV_API_ENDPOINT}/role/<string:Role_ID>/<string:Role_Name>/<string:Role_Desc>`
        axios
            .post(apiEndpoint)
            .then((res) => {
                resolve(res.data)
            })
            .catch((err) => {
                console.log(err);
                reject('Fail to fetch all courses, check WAMP/MAMP server')
            })
    })
}