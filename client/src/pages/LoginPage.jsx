import { useEffect } from 'react';
import { useRouteError } from 'react-router-dom';


export default function LoginPage(){
	const error = useRouteError();

	useEffect(() => {
		window.location.href =
		getLoginUrl()
	}, []);
	return null;
}

function getLoginUrl(){
	const url = new URL("/api/v1/login",
		"http://0:8082");
	return url;
}
