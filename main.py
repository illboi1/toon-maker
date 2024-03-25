import numpy as np
import cv2 as cv


class ToonMaker:
	@staticmethod
	def image_to_cartoon(img):
		edges = ToonMaker.edges_with_canny(img)
		edges_mask = ToonMaker.mask_by_threshold(edges)

		img_filtered = cv.bilateralFilter(img, d=9, sigmaColor=300, sigmaSpace=300)
		img_cartoon = cv.bitwise_and(img_filtered, img_filtered, mask=edges_mask)

		return img_cartoon

	@staticmethod
	def edges_with_canny(img, lower_threshold=30, upper_threshold=100):
		img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
		img_gray_blured = cv.medianBlur(img_gray, 5)
		edges = cv.Canny(img_gray_blured, threshold1=lower_threshold, threshold2=upper_threshold)

		return edges

	@staticmethod
	def mask_by_threshold(img_gray, threshold=127):
		_, mask = cv.threshold(img_gray, threshold, 255, cv.THRESH_BINARY_INV)
		return mask



if __name__ == '__main__':
	video = cv.VideoCapture('res/20240325_202847.mp4')
	if not video.isOpened():
		print("Read error: Failed to take a camera!")

	fps = video.get(cv.CAP_PROP_FPS)
	wait_msec = int(1 / fps * 1000)

	img_orig = cv.imread('res/ikea_spruttig.jpg')
	img_scale = 0.1

	view_edge = False

	while True:
		valid, frame = video.read()
		if not valid:
			break

		# Process frame
		img = cv.resize(frame, (0, 0), fx=img_scale, fy=img_scale)
		merged = None

		if view_edge: # Show edge-detection process
			edges = ToonMaker.edges_with_canny(img)
			edge_mask = ToonMaker.mask_by_threshold(edges)
			merged = np.hstack((cv.cvtColor(img, cv.COLOR_BGR2GRAY), edges, edge_mask))
		else: # Show toon-conversion process
			img_smooth = cv.bilateralFilter(img, d=9, sigmaColor=300, sigmaSpace=300)
			img_toon = ToonMaker.image_to_cartoon(img)
			merged = np.hstack((img, img_smooth, img_toon))
		cv.imshow('Cartoon Making', merged)

		# Process the key event
		key = cv.waitKey(wait_msec)
		if key == 27: # ESC
			break
		elif key == ord('+') or key == ord('='):
			img_scale += 0.05
		elif key == ord('-') or key == ord('_'):
			img_scale = max(img_scale - 0.05, 0.1)
		elif key == ord('\t'):
			view_edge = not view_edge

	video.release()
	cv.destroyAllWindows()