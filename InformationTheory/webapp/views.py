from django.shortcuts import render
from django.http import HttpResponse
from webapp.lib import project1
from webapp.lib import project2
from webapp.lib import project3
from webapp.lib import project4
from webapp.lib import project5
from webapp.lib import project6
from webapp.lib import RSA

def home(request):
	return render(request, 'webapp/home.html')
   

def huffman(request):
	dict = {}
	text = request.POST.get('text')
	
	RSA_encrypted_text, d, e, n, PHI  = RSA.encrypt(text)
	dict = project1.get_probabilities(RSA_encrypted_text)
	encoded_data, final_seq, root = project2.get_result(dict, RSA_encrypted_text)
	ratio = ((len(RSA_encrypted_text.encode('utf-8'))*8)/len(final_seq))
	ratio = round(ratio, 3)
	text_parity = project4.get_result(final_seq)
	error_text = project5.get_result(text_parity)
	error_corrected_text = project6.get_result(error_text)
	decoded_after_error_text = project3.get_result(root, error_corrected_text)
	RSA_decrypted_text = RSA.decrypt(int(RSA_encrypted_text), d, n).decode("utf-8")
	data = {
		'original': text,
		'encrypted_text': RSA_encrypted_text,
		'encoded': final_seq,
		'ratio':  ratio,
		'encoded_table': encoded_data,
		'prob_table': dict,
		'par_text': text_parity,
		'error_text': error_text,
		'error_corrected_text': error_corrected_text,
		'decoded_after_error_text': decoded_after_error_text,
		'decrypted_text': RSA_decrypted_text
	}
	return render(request, 'webapp/result.html', {'data':data})

def RSA_encrypt(request):
	text = request.POST.get('text')
	RSA_encrypted_text, d, e, n, phi = RSA.encrypt(text)
	RSA_decrypted_text = RSA.decrypt(RSA_encrypted_text, d, n).decode("utf-8")

	data = {
		'original_text': text,
		'encrypted_text': RSA_encrypted_text,
		'decrypted_text': RSA_decrypted_text,
		'PHI': phi,
		'n': n,
		'd': d,
		'e': e
	}
	return render(request, 'webapp/RSA_result.html', {'data':data})