import { useLoaderData } from 'react-router-dom';
import { useEffect, useState } from 'react';
import ErrorPage from './ErrorPage';

export default function UserDashboard(){
	const userId = useLoaderData();
	const [user, setUser] = useState(null);

	useEffect(async () => {
		const response = await getUserDetails({
			owner_id: userId
		})
		setUser(response.data);
	}, [userId]);

	if (!user){
		return (<p>Hold on, we're fetching your data...</p>)
	}
	if (user?.message) {
		return (<ErrorPage context={user.message}/>)
	}
	return (
		<>
			<p>`${user.first_name} ${user.last_name}'s dashboard`</p>
		</>
	);
}

export function loader({ request }){
	const requestURL = new URL(request.url);
	const params = URLSearchParams(requestURL.search);
	const searchValues = [...params];
	const userId = searchValues[0]["user_id"];

	console.log("DASHBOARD USER_ID: ", userId);
	return userId;
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
