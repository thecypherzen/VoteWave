/* Defines the landing page */
import Heading from '../components/Heading';
import NavBar from '../components/NavBar';
import Section, {
	SectionImage,
	SectionText
} from '../components/Section';
import { faArrowRight } from '@fortawesome/free-solid-svg-icons';
import styles from '../styles/section.module.css';

export default function Landing(){
	return (
		<>
		<NavBar />
		<Section id="hero-section" clsname={styles.landingSection}>
			<SectionText
				heading="Goodbye to boring voting experiences."
				body="Now you can vote, play and chat all at once. Join a poll or election to begin."
				button={{
					href: "/activities",
					text: "Join activity",
					clist: ["btn", "btn-secondary"],
					icon: faArrowRight
				}}/>
			<SectionImage />
		</Section>
		<Heading clist={[styles.center]}
				swoosh={[styles.swoosh]}
				main={true}
				text="Features" />
		<Section id="features-section1" clsname={styles.landingSection}>
			<SectionText
				heading="Create elections and opinion polls."
				body="Share links to your event and invite friends to participate...You'd get a hang of it when you create one."
				button={{
					href: "/login",
					text: "Get started",
					clist: ["btn", "btn-secondary"],
					icon: faArrowRight
				}}/>
			<SectionImage />
		</Section>
		<Section id="features-section2" clsname={styles.landingSection}>
			<SectionImage />
			<SectionText
				heading="Keep the room alive, no dulling!"
				body="While events are ongoing, engage with other participants in the dedicated chatroom"
				button={{
					href: "/login",
					text: "Try it now",
					clist: ["btn", "btn-secondary"],
					icon: faArrowRight
				}}/>
		</Section>

		<Section id="features-section3" clsname={styles.landingSection}>
			<SectionText
				heading="Share voting results with participants."
				body="It's automatic, but you could also download them."
				button={{
					href: "/login",
					text: "Try it now",
					clist: ["btn", "btn-secondary"],
					icon: faArrowRight
				}}/>
			<SectionImage />
		</Section>

		<Section id="features-section4" clsname={styles.landingSection}>
			<SectionImage />
			<SectionText
				heading="Access trivia games in games area."
				body="You don't need an account to play...give it a try."
				button={{
					href: "/login",
					text: "Let's go",
					clist: ["btn", "btn-secondary"],
					icon: faArrowRight
				}}/>
		</Section>

		</>
	);
}