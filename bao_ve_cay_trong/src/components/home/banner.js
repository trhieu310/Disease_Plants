import React from 'react';
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

const bannerImg = require('assests/imgs/banner.png');
const { width, height } = Image.resolveAssetSource(bannerImg);

const Banner = () => {
	return (
		<View style={[styles.container]}>
			<Image
				resizeMethod='resize'
				resizeMode='contain'
				style={[styles.canvas]}
				source={require('assests/imgs/banner.png')}
			/>
		</View>
	);
};

const styles = StyleSheet.create({
	container: {
		// flex: 1,
		justifyContent: 'center',
		alignItems: 'stretch',
		position: 'relative',
		minHeight: 250,
	},
	canvas: {
		height: undefined,
		width: '100%',
		aspectRatio: width / height,
	},
	flex1: {
		flex: 1,
	},
});

export default Banner;
