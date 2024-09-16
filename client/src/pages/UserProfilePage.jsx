import axios from 'axios';

export default function UserProfilePage(){
	return (<></>);
}

export function loader(){
	/* load a user's profile */
	return null;
}

export function  getUserDetails({userId}){
	try {
		const res = axios.get(
			`http://0:8082/users/${userId}`
		);
		return {error: false, data: res.data}
	} catch (error) {
		return {error: true, data: error}
	}
}