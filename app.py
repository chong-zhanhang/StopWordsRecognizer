from flask import Flask, render_template, request
import DFA_Recognizer
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file_upload = request.files['text_file']
        
        if file_upload:
            text = file_upload.read().decode('utf-8')
        else:
            text = """Malaysia
From Wikipedia, the free encyclopedia
Malaysia is a federal constitutional monarchy located in Southeast Asia. It consists of thirteen states 
and three federal territories and has a total landmass of 329,847 square kilometres (127,350 sq mi) 
separated by the South China Sea into two similarly sized regions, Peninsular Malaysia and East 
Malaysia (Malaysian Borneo). Peninsular Malaysia shares a land and maritime border with Thailand 
and maritime borders with Singapore, Vietnam, and Indonesia. East Malaysia shares land and 
maritime borders with Brunei and Indonesia and a maritime border with the Philippines. The capital 
city is Kuala Lumpur, while Putrajaya is the seat of the federal government. By 2015, with a population 
of over 30 million, Malaysia became 43rd most populous country in the world. The southernmost 
point of continental Eurasia, Tanjung Piai, is in Malaysia, located in the tropics. It is one of 17 
megadiverse countries on earth, with large numbers of endemic species.
Malaysia has its origins in the Malay kingdoms present in the area which, from the 18th century, 
became subject to the British Empire. The first British territories were known as the Straits 
Settlements, whose establishment was followed by the Malay kingdoms becoming British 
protectorates. The territories on Peninsular Malaysia were first unified as the Malayan Union in 1946. 
Malaya was restructured as the Federation of Malaya in 1948, and achieved independence on 31 
August 1957. Malaya united with North Borneo, Sarawak, and Singapore on 16 September 1963, with 
is being added to give the new country the name Malaysia. Less than two years later in 1965, 
Singapore was expelled from the federation.
Since its independence, Malaysia has had one of the best economic records in Asia, with its GDP 
growing at an average of 6.5% per annum for almost 50 years. The economy has traditionally been 
fuelled by its natural resources, but is expanding in the sectors of science, tourism, commerce and 
medical tourism. Today, Malaysia has a newly industrialised market economy, ranked third largest in 
Southeast Asia and 29th largest in the world. It is a founding member of the Association of Southeast 
Asian Nations, the East Asia Summit and the Organisation of Islamic Cooperation, and a member of 
Asia-Pacific Economic Cooperation, the Commonwealth of Nations, and the Non-Aligned Movement."""

        if request.form['patterns'] == "":
            patterns = ["the, and, of, to, in, a, is, that, for, it, as, was, with, on, at"]
        else:
            patterns = request.form['patterns'].split(',')

        results = DFA_Recognizer.process_text(text, patterns)

        return render_template('results.html', results=results)
    
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
