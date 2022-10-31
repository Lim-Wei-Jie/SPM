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

// Get specific Job Role details using Job Role ID / Name
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
                reject('Fail to fetch job role details, check WAMP/MAMP server')
            })
    })
}

// Get all skills assigned to Job Role using Job Role ID
export function getSkillsByRole(jobRoleID) {
    return new Promise((resolve, reject) => {
        let apiEndpoint = `${import.meta.env.VITE_APP_DEV_API_ENDPOINT_MANAGER}/role/getskill/${jobRoleID}`
        axios
            .get(apiEndpoint)
            .then((res) => {
                resolve(res.data.data.Skill)
            })
            .catch((err) => {
                reject(err.response.data)
            })
    })
}

// Get all Courses that fulfils the Skill using Skill ID
export function getCoursesBySkill(skillID) {
    return new Promise((resolve, reject) => {
        let apiEndpoint = `${import.meta.env.VITE_APP_DEV_API_ENDPOINT_MANAGER}/skill/getcourse/${skillID}`
        axios
            .get(apiEndpoint)
            .then((res) => {
                resolve(res.data.data.Course)
            })
            .catch((err) => {
                reject(err.response.data)
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
                reject('Fail to create role, check WAMP/MAMP server')
            })
    })
}

// Update job role
export function updateRole(roleDetails, removeSkillsIDArr, addSkillsIDArr) {
    console.log(roleDetails.roleName);
    const removeSkills = JSON.parse(JSON.stringify(removeSkillsIDArr))
    const addSkills = JSON.parse(JSON.stringify(addSkillsIDArr))
    return new Promise((resolve, reject) => {
        let updateEndpoint = `${import.meta.env.VITE_APP_DEV_API_ENDPOINT_MANAGER}/role/update/${roleDetails.roleID}/${roleDetails.roleName}/${roleDetails.roleDesc}`
        let assignRemoveEndpoint = `${import.meta.env.VITE_APP_DEV_API_ENDPOINT_MANAGER}/role/roledeleteskills/${roleDetails.roleID}/${removeSkills}`
        let assignAddEndpoint = `${import.meta.env.VITE_APP_DEV_API_ENDPOINT_MANAGER}/role/roleassignskills/${roleDetails.roleID}/${addSkills}`
        axios.all([
            axios.put(updateEndpoint),
            axios.post(assignRemoveEndpoint),
            axios.post(assignAddEndpoint)
        ])
        .then(axios.spread((obj1, obj2, obj3) => {
            console.log(obj1.data);
            console.log(obj2.data);
            console.log(obj3.data);
        }))
        .catch((err) => {
            console.log(err.message);
            reject('Fail to delete role, check WAMP/MAMP server');
        })
    })
}

// Delete job role
export function deleteRole(roleID) {
    return new Promise((resolve, reject) => {
        let apiEndpoint = `${import.meta.env.VITE_APP_DEV_API_ENDPOINT_MANAGER}/role/delete/${roleID}`
        axios
            .post(apiEndpoint)
            .then((res) => {
                resolve(res.data)
            })
            .catch((err) => {
                console.log(err.message);
                reject('Fail to delete role, check WAMP/MAMP server');
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

// Get specific course using course name
export function getCourseDetails(Course_Name) {
    return new Promise((resolve, reject) => {
        let apiEndpoint = `${import.meta.env.VITE_APP_DEV_API_ENDPOINT_COURSE}/searchcourse/${Course_Name}`
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

// Delete skill

// Get all courses
export function getAllCourses() {
    return new Promise((resolve, reject) => {
        let apiEndpoint = `${import.meta.env.VITE_APP_DEV_API_ENDPOINT_COURSE}/course`
        axios
            .get(apiEndpoint)
            .then((res) => {
                resolve(res.data.courses)
            })
            .catch((err) => {
                console.log(err);
                reject('Fail to fetch all courses, check WAMP/MAMP server')
            })
        })
}

//LEARNING JOURNEY

// Get all registration
export function getAllRegistration() {
    return new Promise((resolve, reject) => {
        let apiEndpoint = `${import.meta.env.VITE_APP_DEV_API_ENDPOINT_COURSE}/Registration`
            axios
            .get(apiEndpoint)
            .then((res) => {
                resolve(res.data.data)
            })
            .catch((err) => {
                console.log(err.message);
                reject('Fail to fetch all registrations, check WAMP/MAMP server')
            })
    })
}

// Get all registration number
export function getAllRegistrationNo() {
    return new Promise((resolve, reject) => {
        let apiEndpoint = `${import.meta.env.VITE_APP_DEV_API_ENDPOINT_COURSE}/Registration`
            axios
            .get(apiEndpoint)
            .then((res) => {
                resolve(res.data.data.registration.length + 1)
            })
            .catch((err) => {
                console.log(err.message);
                reject('Fail to fetch all registrations, check WAMP/MAMP server')
            })
    })
}

export function getAllLJPSNo() {
    return new Promise((resolve, reject) => {
        let apiEndpoint = `${import.meta.env.VITE_APP_DEV_API_ENDPOINT_COURSE}/LJPS_Assignment`
            axios
            .get(apiEndpoint)
            .then((res) => {
                resolve(res.data.data.maps.length + 1)
            })
            .catch((err) => {
                console.log(err.message);
                reject('Fail to fetch all registrations, check WAMP/MAMP server')
            })
    })
}

// Get registration with Staff ID
export function getRegistration(staffID) {
    return new Promise((resolve, reject) => {
        let apiEndpoint = `${import.meta.env.VITE_APP_DEV_API_ENDPOINT_COURSE}/Registration/${staffID}`
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

// create registration
export function createRegistration(regID, courseID, staffID, regStatus, completionStatus) {
    return new Promise((resolve, reject) => {
        let apiEndpoint = `${import.meta.env.VITE_APP_DEV_API_ENDPOINT_COURSE}/Registration/addRegis/${regID}/${courseID}/${staffID}/${regStatus}/${completionStatus}`
        axios
        .post(apiEndpoint)
            .then((res) => {
                resolve(res.data)
            })
            .catch((err) => {
                console.log(err.message);
                reject('Fail to create registration, check WAMP/MAMP server');
            })
    })
}


// Get Learning Journeys with Staff ID
export function getLJs(staffID) {
    return new Promise((resolve, reject) => {
        let apiEndpoint = `${import.meta.env.VITE_APP_DEV_API_ENDPOINT_COURSE}/LJAssign/${staffID}`
        axios
            .get(apiEndpoint)
            .then((res) => {
                resolve(res.data.data.deets)
            })
            .catch((err) => {
                console.log(err);
                reject('Fail to fetch learning journeys of staff, check WAMP/MAMP server')
            })
    })
}

// create LJ assignment
export function createLJAssign(courseID, roleID, staffID, ljpsID) {
    return new Promise((resolve, reject) => {
        let apiEndpoint = `${import.meta.env.VITE_APP_DEV_API_ENDPOINT_COURSE}/AddLJAssign/${staffID}/${roleID}/${courseID}/${ljpsID}`
        axios
        .post(apiEndpoint)
            .then((res) => {
                resolve(res.data)
            })
            .catch((err) => {
                console.log(err.message);
                reject('Fail to create registration, check WAMP/MAMP server');
            })
    })
}

export function getRoleNameByID(jobID) {
    return new Promise((resolve, reject) => {
        let apiEndpoint = `${import.meta.env.VITE_APP_DEV_API_ENDPOINT_MANAGER}/role/${jobID}`
        axios
            .get(apiEndpoint)
            .then((res) => {
                resolve(res.data.data.Role[0].Role_Name)
            })
            .catch((err) => {
                console.log(err);
                reject('Fail to fetch registration of staff, check WAMP/MAMP server')
            })
    })
}

export function getRoleByID(jobID) {
    return new Promise((resolve, reject) => {
        let apiEndpoint = `${import.meta.env.VITE_APP_DEV_API_ENDPOINT_MANAGER}/role/${jobID}`
        axios
            .get(apiEndpoint)
            .then((res) => {
                resolve(res.data.data.Role[0])
            })
            .catch((err) => {
                console.log(err);
                reject('Fail to fetch registration of staff, check WAMP/MAMP server')
            })
    })
}

export function getSkillIdByCourseName(CourseID) {
    return new Promise((resolve, reject) => {
        let apiEndpoint = `${import.meta.env.VITE_APP_DEV_API_ENDPOINT_MANAGER}/skill_course_assignment`
        axios
            .get(apiEndpoint)
            .then((res) => {
                var assignments = res.data.data.maps
                var b = []
                for (var a of assignments) {
                    if (CourseID == a.Course_ID) {
                        b.push(a.Skill_ID)
                    }
                }
                resolve(b)
            })
            .catch((err) => {
                console.log(err);
                reject('Fail to fetch registration of staff, check WAMP/MAMP server')
            })
    })
}

export function getStaffCreate() {
    return new Promise((resolve, reject) => {
        let apiEndpoint = `${import.meta.env.VITE_APP_DEV_API_ENDPOINT_COURSE}/Registration`
            axios
            .get(apiEndpoint)
            .then((res) => {
                resolve(res.data.data.registration.length + 1)
            })
            .catch((err) => {
                console.log(err.message);
                reject('Fail to fetch all registrations, check WAMP/MAMP server')
            })
    })
}