import React, { useEffect } from 'react';
import {
	StyleSheet,
	Text,
	View,
	SafeAreaView,
	Image,
	TouchableOpacity,
	FlatList,
} from 'react-native';
import { hasReadExternalStoragePermission } from 'until/permission';
import Icon from 'react-native-vector-icons/FontAwesome5';
import axios from 'axios';

const send = (
	image,
	url = 'http://192.168.1.6:8080/predict',
	options = { method: 'POST', headers: {} },
) => {
	const { method, headers } = options;
	// console.warn(REACT_APP_ENV_POINT);

	const img = {
		uri: image,
		type: 'image/jpeg',
		name: `disease.jpg`,
	};

	const body = new FormData();
	body.append('img', img);
	// body.append('img2', img);
	// body.append('disease', 'aaaaaaaaaaaaaaaa');
	console.log(body, image);

	return axios({
		url: url,
		data: body,
		method: method,
		headers: {
			Accept: 'application/json',
			'Content-Type': 'multipart/form-data',
			...headers,
		},
	})
		.then(rs => rs.data)
		.catch(e => console.error(e));
};

const PreviewImage = ({ navigation, route, ...props }) => {
	const { listImage = [] } = route.params;

	hasReadExternalStoragePermission()
		.then(() => console.log('hasReadExternalStoragePermission'))
		.catch(e => console.warn(e));

	// const listImageUri = listImage.map(
	// 	entry => entry.uri /* .split('//')[1] */,
	// );

	const predictImage = () => {
		listImage.map(img => {
			send(img.uri)
				.then(rs => console.log('Success:::', rs))
				.catch(e => console.error(e));
		});
	};

	// axios
	// 	.get('http://192.168.1.9:8080/list')
	// 	.then(rs => rs.data)
	// 	.then(console.log);

	const handleBack = () => navigation.goBack();

	const renderImageItem = ({ item, index, separators }) => {
		return (
			<View key={item.uri} style={styles.boudingBox}>
				<Image
					style={[styles.image, { aspectRatio: item.width / item.height }]}
					source={{ uri: item.uri }}
				/>
				{/* <Text>{item.uri}</Text> */}
			</View>
		);
	};

	return (
		<SafeAreaView style={[styles.fullScreen]}>
			<View style={styles.fullScreen}>
				<View style={styles.navbar}>
					<TouchableOpacity style={styles.backButton} onPress={handleBack}>
						<Icon name='chevron-left' size={30} color='#484848' />
					</TouchableOpacity>
				</View>
				<FlatList
					data={listImage}
					renderItem={renderImageItem}
					keyExtractor={item => item.uri}
				/>
				<View style={styles.bottomActions}>
					<TouchableOpacity onPress={predictImage} style={styles.scanButton}>
						<Text style={styles.text}>Chuẩn đoán</Text>
					</TouchableOpacity>
				</View>
			</View>
		</SafeAreaView>
	);
};

const styles = StyleSheet.create({
	fullScreen: {
		width: '100%',
		height: '100%',
		backgroundColor: 'white',
	},
	navbar: {
		width: '100%',
		height: 56,
		display: 'flex',
		justifyContent: 'center',
		alignItems: 'flex-start',
		backgroundColor: 'white',
		borderBottomColor: '#e4e4e4',
		borderBottomWidth: 1,
	},
	image: {
		width: '100%',
	},
	backButton: {
		width: 50,
		height: '100%',
		// borderColor: 'red',
		// borderWidth: 2,
		// borderStyle: 'solid',
		display: 'flex',
		justifyContent: 'center',
		alignItems: 'center',
	},
	boudingBox: {
		paddingVertical: 16,
		paddingHorizontal: 16,
	},
	bottomActions: {
		width: '100%',
		height: 64,
		display: 'flex',
		justifyContent: 'center',
		alignItems: 'center',
		backgroundColor: 'white',
		borderTopColor: '#e4e4e4',
		borderTopWidth: 1,
	},
	scanButton: {
		width: '50%',
		height: '90%',
		// borderColor: '#d2ffd0',
		// borderWidth: 1,
		// borderStyle: 'solid',

		display: 'flex',
		justifyContent: 'center',
		alignItems: 'center',
		borderRadius: 4,
		backgroundColor: '#28a745',
	},
	text: {
		fontSize: 24,
		color: 'white',
	},
});

export default PreviewImage;
