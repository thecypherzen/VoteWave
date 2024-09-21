import {
	Form, useLoaderData,
	useRouteError
} from 'react-router-dom';
import { useEffect, useState } from 'react';
import axios from 'axios';
import Wrapper from '../components/Wrapper';
import styles from '../styles/onboarding.module.css';
import { faFileArrowUp } from '@fortawesome/free-solid-svg-icons';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';

export default function OnBoardingPage(){
	const userData = useLoaderData();
	const error = useRouteError();
	const [avatar, setAvatar] = useState(null);
	const [message, setMessage] = useState(null);
	const [progress, setProgress] = useState({started: false, percent: 0});
	const [anyError, setAnyError ] = useState(false);

	async function uploadFile(){
		if (!avatar){
			console.log("No file selected yet");
			setMessage("No file selected yet");
			return;
		}
		const formData = new FormData();
		formData.append("avatar", avatar);
		try {
			setMessage("Uploading...");
			setProgress((prev) => {
				return {...prev, started: true};
			});
			const response = await axios.post(`http://httpbin.org/post`, formData,
				{onUploadProgress: (event) => {
					setProgress((prev) => {
						return {
							...prev,
							percent: Math.floor(event.progress * 100)}
					});
				}
			})
			console.log(response);
			setMessage("Done.");
		} catch (err) {
			setAnyError(true);
			setErrMsg(err.message);
		}
	}
	if (message === "Done.") {
		setTimeout(() => {
			document.getElementById("message").style.display = "none";
			document.getElementById("progress").style.display = "none";
		}, 1000);
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
						<Form id="form" method="post" className={styles.form}>
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
									<input type="text" name="first_name" id="last_name" placeholder='Chosen'
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
									autoComplete="on"/>
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

							<div className={`${styles.formItem} ${styles.fileArea}`}>
								<div className={styles.input}>
									<label htmlFor="avatar">Profile Photo</label>
									<input type="file" name="avatar" id="avatar" placeholder="A photo of yourself"
									required aria-required
									onChange={(e) => setAvatar(e.target.files[0])} />
								</div>
								<button className={styles.uploadBtn}
									type="button"
									onClick={ uploadFile }>
										<FontAwesomeIcon icon={faFileArrowUp} />
								</button>
							</div>
							<div className={styles.messageArea}>
									{
										message && <p className={`${styles.message} ${!anyError ? styles.success
											: styles.error}`}
											id="message">{message}</p>
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
						</Form>
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
