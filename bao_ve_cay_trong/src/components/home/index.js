import React, { useEffect } from 'react';
import {
	StyleSheet,
	Text,
	View,
	SafeAreaView,
	ScrollView,
	Image,
	Dimensions,
	Platform,
	TouchableOpacity,
} from 'react-native';

import Banner from './banner';
import Crops from './crops';
import Screens from 'until/screens';

const Home = ({ navigation, ...props }) => {
	// useEffect(() => {
	// 	setTimeout(() => {
	// 		navigation.navigate(Screens.CAPTURE, {
	// 			name: 'Home',
	// 			crop: 'rice',
	// 		});
	// 		console.log('Navigating');
	// 	}, 5000);
	// }, []);

	return (
		<SafeAreaView style={[styles.fullScreen]}>
			<ScrollView>
				<View style={styles.fullScreen}>
					<Banner />
					<Crops />
				</View>
			</ScrollView>
		</SafeAreaView>
	);
};

const styles = StyleSheet.create({
	fullScreen: {
		width: '100%',
		height: '100%',
		backgroundColor: 'white',
	},
});

export default Home;
