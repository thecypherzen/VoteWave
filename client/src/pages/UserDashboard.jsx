import {
	useLoaderData, Outlet
} from 'react-router-dom';
import { useEffect, useState } from 'react';
import axios from 'axios';
import ErrorPage from './ErrorPage';
import Wrapper from '../components/Wrapper';
import Alert from '../components/Alert';
import PageNav from '../components/PageNav';
import styles from '../styles/userdashboard.module.css';


export default function UserDashboard(){
	const userId = useLoaderData();
	const [user, setUser] = useState(null);
	const [message, setMessage] = useState(null);
	const [errorOccured, setErrorOccured] = useState(false);

	if (!userId) {
		return (<ErrorPage context="User unknown. Are you logged in?"/>)
	}
	useEffect(() => {
		getUserDetails({owner_id: userId})
		.then(response => {
			setUser(response.data);
			axios.get(`http://0:8082/api/v1/users/${userId}/avatar`,
				{responseType: "blob"}
			)
			.then(response => {
				const imgURL = URL.createObjectURL(response.data);
				setUserIcon(imgURL);
			}).catch(error => {
				if(error.status === 404) {
					setUserIcon(new URL("../assets/default_user_icon.png"));
				}
				if (error?.response?.data){
					setMessage(error.response.data?.error || error.message);
				} else {
					setMessage(error.message);
				}
				setErrorOccured(true);
			});
		})
		.catch(error => {
			console.log(error);
			setErrorOccured(true);
			setMessage(error.message);
			setUser(error);
		})

	}, [userId]);

	if (!user){
		return (
			<main className={styles.bgPrimary}>
				<Wrapper clist={[styles.tempWrapper]}>
					<h3> Loading...</h3>
				</Wrapper>
			</main>
		)
	}
	if (user?.message) {
		console.log("an error occured");
		return (<ErrorPage context={user.message}/>)
	}
	return (
		<main className={styles.dWrapper}>
			<section className={styles.navArea}>
				<PageNav owner={""}/>
			</section>
			<section className={styles.mainArea}>
				<Alert message={message} error={errorOccured}/>
				<Outlet />
			</section>
		</main>
	);
}



export function loader({ params }){
	return params?.userId ?? null;
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


function setUserIcon(url){
	const userIcon = document.getElementById("nav-owner-icon");
	if (userIcon){
		userIcon.style.backgroundImage = `url(${url})`;
		userIcon.style.backgroundPosition = "center center";
		userIcon.style.backgroundRepeat = "no-repeat";
		userIcon.style.backgroundSize = "cover";
	}
}