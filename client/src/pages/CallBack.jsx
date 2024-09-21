import {
	useLoaderData, useNavigate,
	useRouteError
} from 'react-router-dom';
import { useState, useEffect } from 'react';
import axios from 'axios';
import EmailVerfivationPage from './EmailVerificationPage';


export default function CallBack(){
	const {
		email_verified, access_token=null,
	} = useLoaderData();
	const [verified, setVerified] = useState(email_verified === "True");
	const navigate = useNavigate();
	const error = useRouteError();

	console.log("INTITIAL VERIFIED VALUE: ", verified);

	useEffect(() => {
		if (!verified) {
			verify_email(access_token, setVerified);
		}
		else {
			navigate("/login");
		}
	}, [verified]);

	if (!verified){
		return (
			<EmailVerfivationPage />
		);
	}
	return null;
}


export function loader({request}){
	const requestURL = new URL(request.url);
	const params = new URLSearchParams(requestURL.search);
	const values = [...params]
	const  result = {}

	for (let i = 0; i < values.length; i++){
		result[values[i][0]] = values[i][1];
	}
	return result;
}

function verify_email(accessToken, statusSetter){
	const SAFEINTERVAL = 30000;
	async function checkEmailVerified() {
		try {
			const status = await axios.post(`http://0:8082/api/v1/login/verify`, {}, {
				headers : {
					"Authorization": `Bearer ${accessToken}`
				}});
			if (status.data.email_verified){
				statusSetter(true);
			} else {
				console.log("recalling: ", status.data.email_verified);
				setTimeout(checkEmailVerified, SAFEINTERVAL);
			}
		} catch (err) {
			console.log(err);
			setTimeout(checkEmailVerified, SAFEINTERVAL);
		}
	}
	checkEmailVerified();
}