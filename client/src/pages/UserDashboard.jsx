import { useLoaderData } from 'react-router-dom';
import { useEffect, useState } from 'react';
import axios from 'axios';
import ErrorPage from './ErrorPage';
import Button from '../components/Button';
import styles from '../styles/userdashboard.module.css';

export default function UserDashboard(){
	const userId = useLoaderData();
	const [user, setUser] = useState(null);

	if (!userId) {
		return (<ErrorPage context="User unknown. Are you logged in?"/>)
	}
	useEffect(() => {
		getUserDetails({owner_id: userId})
		.then(response => {
			console.log(response);
			setUser(response.data);
		})
		.catch(error => {
			console.log(error);
			setUser(error);
		})

	}, [userId]);
	if (!user){
		return (<p>Hold on, we're fetching your data...</p>)
	}
	if (user?.message) {
		console.log("an error occured");
		return (<ErrorPage context={user.message}/>)
	}
	return (
		<>
			<p>{user.first_name} {user.last_name}'s dashboard</p>
			<div className={styles.logoutBtn}>
				<Button clist={["btn", "btn-secondary"]}
					href="/logout" text="Logout"/>
			</div>
		</>
	);
}

export function loader({ params }){
	return params?.userId ?? null;
}


export async function  getUserDetails({owner_id}){
	console.log(owner_id);
	try {
			const res = await axios.get(
					`http://0:8082/api/v1/users/${owner_id}`
			);
			console.log(res);
			return {error: false, data: res.data}
	} catch (error) {
			return {error: true, data: error}
	}
}
