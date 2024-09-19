import axios from 'axios';

export default function UserProfilePage(){
	return (<></>);
}

export function loader(){
	/* load a user's profile */
	return null;
}

export async function  getUserDetails({owner_id}){
	try {
		const res = await axios.get(
			`http://0:8082/api/v1/users/${owner_id}`
		);
		return {error: false, data: res.data}
	} catch (error) {
		return {error: true, data: error}
	}
}
