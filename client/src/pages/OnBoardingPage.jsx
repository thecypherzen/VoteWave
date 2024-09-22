import {
	Form, useLoaderData,
	useRouteError, useNavigate
} from 'react-router-dom';
import { useEffect, useState } from 'react';
import axios from 'axios';
import Wrapper from '../components/Wrapper';
import styles from '../styles/onboarding.module.css';


export default function OnBoardingPage(){
	const userData = useLoaderData();
	const error = useRouteError();
	const [avatar, setAvatar] = useState(null);
	const [message, setMessage] = useState(null);
	const [progress, setProgress] = useState({started: false, percent: 0});
	const [anyError, setAnyError ] = useState(false);
	const navigate = useNavigate();

	async function upLoadData(event){
		event.preventDefault();
		if (!avatar){
			setMessage("No file selected yet");
			return;
		}
		console.log(event.target);
		const formData = new FormData();
		formData.append("avatar", avatar);
		formData.append("first_name", event.target.first_name.value);
		formData.append("last_name", event.target.last_name.value);
		formData.append("email", event.target.email.value);
		formData.append("dob", event.target.dob.value);
		formData.append("password", event.target.password.value);
		formData.append("security_key", event.target.security_key.value);
		formData.append("username", event.target.username.value);
		console.log("values entered:");
		console.log(Object.fromEntries(formData));

		/* Hide submit btn */
		document.getElementById("submitBtn").style.display = "none";
		try {
			setMessage("Ok, working on that...");
			setProgress((prev) => {
				return {...prev, started: true};
			});
			const response = await axios.post("http://0:8082/api/v1/users/new", formData,
				{
					headers: {
						'Content-Type': 'multipart/form-data'
					},
					onUploadProgress: (event) => {
					setProgress((prev) => {
						return {
							...prev,
							percent: Math.floor(event.progress * 100)}
					});
				}
			})
			console.log(response);
			setMessage("Done.");
			hideProgressBar();
			if (response.status === 200) {
				setMessage("Logging you in now..");
				hideMessage(1000);
				setTimeout(() => {
					navigate("/login");
				}, 2000);
			}
		} catch (error) {
			setAnyError(true);
			if (error.response){
				const data = error.response.data;
				const email = data?.context?.email;
				const uname = data?.context?.username;
				if (email || uname){
					setMessage(`${email && "email"} \
						${email && uname && "and"} \
						${uname && "username"} \
						already taken`)
				} else {
					setMessage(data.error || error.message)
				}
			} else {
				setMessage(error.message);
			}
			console.log(err);
			hideMessage();
			hideProgressBar();
			unhideSubmitBtn();
		}
	}
	return (
		<>
			<section className={styles.onboardingArea}>
				<Wrapper clist={[styles.wrapper]}>
					<div className={styles.mainArea}>
						<h1>Welcome <br/>{userData.first_name}</h1>
						<p>Kindly complete this form so we can complete your login</p>
					</div>
					<div className={styles.formArea}>
						<div id="alert" className={styles.hide}>
							<p className={styles.alertMessage}></p>
						</div>
						<form id="form" method="post" className={styles.form}
							onSubmit={(e) => upLoadData(e)}>
							<div className={styles.nameDiv}>
								<div className={styles.formItem}>
									<label htmlFor="first_name">First Name</label>
									<input type="text" name="first_name"
									id="first_name"
									defaultValue={userData.first_name}
									required aria-required autoComplete="on"/>
								</div>

								<div className={styles.formItem}>
									<label htmlFor="last_name">Last Name</label>
									<input type="text" name="last_name" id="last_name" placeholder='Chosen'
									defaultValue={
										userData.last_name !== 'None' ? userData.last_name
										: ""
									}
									autoComplete="on"/>
								</div>
							</div>

							<div className={styles.randDiv}>
								<div className={styles.formItem}>
									<label htmlFor="email">Email</label>
									<input type="email" name="email" id="email"
									defaultValue={userData.email}
									required aria-required
									autoComplete="on" disabled/>
								</div>

								<div className={styles.formItem}>
									<label htmlFor="dob">Date of birth</label>
									<input type="date" name="dob" id="dob"
									placeholder="yyyy/mm/dd"
									required aria-required
									autoComplete="on"/>
								</div>
							</div>
							<div className={styles.formItem}>
								<label htmlFor="username">
									Username
								</label>
								<input type="text" name="username" id="username"
								placeholder="your username"
								defaultValue={
									userData.nicknname !== 'None' ? userData.nickname
									: ""
								}
								autoComplete="on"/>
							</div>
							<div className={styles.randDiv}>
								<div className={styles.formItem}>
									<label htmlFor="password">Your password</label>
									<input type="password" name="password" id="password" placeholder='should match your login password'
									required aria-required/>
									<i>this should match your login password if you signed in with one for api login.</i>
								</div>
								<div className={styles.formItem}>
									<label htmlFor="security_key">Security Key</label>
									<input type="password" name="security_key" id="security_key" placeholder="a key you'd remember"
									required aria-required />
									<i>you'd need this to confirm sensitive actions on your account.</i>
								</div>
							</div>

							<div className={`${styles.formItem} ${styles.fileArea}`}>
								<div className={styles.input}>
									<label htmlFor="avatar">Profile Photo</label>
									<input type="file" name="avatar" id="avatar" placeholder="A photo of yourself"
									required aria-required
									onChange={(e) => setAvatar(e.target.files[0])} />
								</div>
							</div>
							<div className={styles.btnDiv}>
								<button id="submitBtn" className={styles.submitBtn}>
									Onboard me
								</button>
							</div>
							<div className={styles.messageArea}>
								{
									message &&
									<p className={`${styles.message} ${!anyError ? styles.success
										: styles.error}`}
										id="message">
											{message}
									</p>
								}
								{
									progress.started &&
									<progress max="100"
										value={progress.percent}
										className={styles.progress}
										id="progress">
									</progress>
								}
								</div>
						</form>
					</div>
				</Wrapper>
			</section>
		</>
	);
}


export function loader({ request }){
	const requestURL = new URL(request.url);
	const params = new URLSearchParams(requestURL.search);
	const searchValues = [...params];
	const result = {}

	for (let i = 0; i < searchValues.length; i++){
		result[searchValues[i][0]] = searchValues[i][1];
	}
	return result;
}

function hideProgressBar(){
	setTimeout(() => {
		const progress = document.getElementById("progress");
		if (progress){
			progress.style.display = "none";
		}
	}, 500);
}

function hideMessage(offset){
	setTimeout(() => {
		document.getElementById("message").style.display = "inline-block";
	}, offset);
}

function unhideSubmitBtn(){
	setTimeout(() => {
		document.getElementById("submitBtn").style.display = "inline-block";
	}, 1000);
}