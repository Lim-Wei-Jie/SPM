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

// Get specific skills using Job Role ID / Name
export function getSkills(jobRoleName) {
    return new Promise((resolve, reject) => {
        let apiEndpoint = `${import.meta.env.VITE_APP_DEV_API_ENDPOINT}/role/name/${jobRoleName}/skills`
        axios
            .get(apiEndpoint)
            .then((res) => {
                resolve(res.data.data.books)
            })
            .catch((err) => {
                console.log(err);
                reject('Fail to fetch all skills, check WAMP/MAMP server')
            })

    })
}

// Get specific courses using skill ID / Name
export function getCourses(skill_ID) {
    return new Promise((resolve, reject) => {
        let apiEndpoint = `${import.meta.env.VITE_APP_DEV_API_ENDPOINT}/role/getcourse/${skill_ID}`
        axios
            .get(apiEndpoint)
            .then((res) => {
                resolve(res.data.data.courses)
            })
            .catch((err) => {
                console.log(err);
                reject('Fail to fetch all courses, check WAMP/MAMP server')
            })

    })
}

// Create new job role
export function handleNewJobRole() {

}

// Delete job role
export function handleDeleteJob() {

}

// Remove course of a skill in a job
export function handleRemoveCourse() {

}