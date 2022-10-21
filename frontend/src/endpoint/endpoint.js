import axios from "axios";

// Get all Job Roles
export function getAllRoles() {
    return new Promise((resolve, reject) => {
        let apiEndpoint = `${import.meta.env.VITE_APP_DEV_API_ENDPOINT_MANAGER}/role`
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
        let apiEndpoint = `${import.meta.env.VITE_APP_DEV_API_ENDPOINT_MANAGER}/role/name/${jobRoleName}`
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
    return new Promise((resolve, reject) => {
        let apiEndpoint = `${import.meta.env.VITE_APP_DEV_API_ENDPOINT_MANAGER}/role/getskill/${jobRoleID}`
        axios
            .get(apiEndpoint)
            .then((res) => {
                resolve(res.data.data.Skill)
            })
            .catch((err) => {
                console.log(err);
                reject('Fail to fetch all skills, check WAMP/MAMP server')
            })
    })
}

// Get specific courses using skill ID / Name
export function getCoursesBySkill(skillID) {
    return new Promise((resolve, reject) => {
        let apiEndpoint = `${import.meta.env.VITE_APP_DEV_API_ENDPOINT_MANAGER}/skill/getcourse/${skillID}`
        axios
            .get(apiEndpoint)
            .then((res) => {
                resolve(res.data.data.Course)
            })
            .catch((err) => {
                console.log(err);
                reject('Fail to fetch all courses, check WAMP/MAMP server')
            })
    })
}

// Create job role
export function createRole(newJobRoleData) {
    var role_id = newJobRoleData[0];
    var role_name = newJobRoleData[1];
    var role_des = newJobRoleData[2];
    // var BE_error = false;
    // var job_err_msg = '';

    return new Promise((resolve, reject) => {
        let apiEndpoint = `${import.meta.env.VITE_APP_DEV_API_ENDPOINT_MANAGER}/role/${role_id}/${role_name}/${role_des}`
        axios
            .post(apiEndpoint)
            .then((res) => {
                resolve(res.data)
            })
            .catch((err) => {
                console.log(err.message);
                // job_err_msg = err.message;
                // BE_error = true;
                reject('Fail to create role, check WAMP/MAMP server');
                // if(err.code == '400'){
                //     err_msg = "Role already exists.";
                //     BE_error = true;
                // }
                // else if (err.code == '500'){
                //     err_msg = "An error occurred creating the Role.";
                //     BE_error = true;
                // }
                // else{
                //     reject('Fail to create role, check WAMP/MAMP server')
                // }
            })
    })
}

// Get all Skills
export function getAllSkills() {
    return new Promise((resolve, reject) => {
        let apiEndpoint = `${import.meta.env.VITE_APP_DEV_API_ENDPOINT_MANAGER}/skill`
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

// Mapping skills to role
export function mapSkillsToJob(skillstoJobRoleData) {
    var role_id = skillstoJobRoleData[0];
    var skills_id = skillstoJobRoleData[1];

    return new Promise((resolve, reject) => {
        let apiEndpoint = `${import.meta.env.VITE_APP_DEV_API_ENDPOINT_MANAGER}/role/roleassignskills/${role_id}/${skills_id}/`
        axios
            .post(apiEndpoint)
            .then((res) => {
                resolve(res.data.data)
            })
            .catch((err) => {
                console.log(err.message);
                reject('Fail to fetch all skills, check WAMP/MAMP server')
            })
    })
}

// Delete job role
export function deleteRole(roleDetailsID) {
  
    return new Promise((resolve, reject) => {
        let apiEndpoint = `${import.meta.env.VITE_APP_DEV_API_ENDPOINT_MANAGER}/role/delete/${roleDetailsID}`
        axios
        .post(apiEndpoint)
            .then((res) => {
                resolve(res.data)
            })
            .catch((err) => {
                console.log(err.message);
                reject('Fail to create role, check WAMP/MAMP server');
            })
    })
}

// Get specific course using course name
export function getCourseDetails(Course_Name) {
    return new Promise((resolve, reject) => {
        let apiEndpoint = `${import.meta.env.VITE_APP_DEV_API_ENDPOINT_COURSE}/searchcourse/${Course_Name}`
        
//LEARNING JOURNEY

// Get all registration
export function getAllRegistration() {
    return new Promise((resolve, reject) => {
        let apiEndpoint = `${import.meta.env.VITE_APP_DEV_API_ENDPOINT2}/Registration`
            axios
            .get(apiEndpoint)
            .then((res) => {
                resolve(res.data.data)
            })
            .catch((err) => {
                console.log(err.message);
                reject('Fail to fetch all skills, check WAMP/MAMP server')
            })
    })
}

// Get registration with Staff ID
export function getRegistration(staffID) {
    return new Promise((resolve, reject) => {
        let apiEndpoint = `${import.meta.env.VITE_APP_DEV_API_ENDPOINT2}/Registration/${staffID}`
        axios
            .get(apiEndpoint)
            .then((res) => {
                resolve(res.data.registration)
            })
            .catch((err) => {
                console.log(err);
                reject('Fail to fetch registration of staff, check WAMP/MAMP server')
            })
    })
}