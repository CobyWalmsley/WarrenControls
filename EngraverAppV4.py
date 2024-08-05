
##THIS CODE IS NOT TO BE FUCKED WITH
#YOU HAVE BEEN WARNED
#kisses, CW
import customtkinter as tk
from PIL import Image

class SampleApp(tk.CTk):
    def __init__(self):
        tk.CTk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)
        tk.set_appearance_mode('Dark')
        tk.set_default_color_theme("dark-blue")
        self.title("Gcode Writer")
        self.geometry("1580x800")

    def switch_frame(self, frame_class):
        """Destroys current frame and replaces it with a new one."""
        new_frame = frame_class(self)
       
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.grid(row=0,column=0)

    
    def mod_coords(self,val,input_string,space_length,space_number):
        length = 7
        if val not in input_string:
            return input_string
        if val in input_string:
            for n in range(len(input_string)):
                if input_string[n]==val:
                    position = n
            if input_string[position+1]=='-':
                length=8
            beginning = input_string[:position+1]
            end = input_string[position+length:]
            number = float(input_string[position+1:position+length])
            number = (number+(space_length*space_number))
            middle = str(number)
            if '-' in middle:
                length2=7
            if '-' not in middle:
                length2=6
            for n in range(10):
                if len(middle)<length2:
                    middle=middle+'0'
            middle2 = middle[0:length2]   
            output_string = beginning+middle2+end
            return output_string

    def rescale_letters(self,val,input_string,rescale_factor):
        length = 7
        if val not in input_string:
            return input_string
        if val in input_string:
            for n in range(len(input_string)):
                if input_string[n]==val:
                    position = n
            if input_string[position+1]=='-':
                length=8
            beginning = input_string[:position+1]
            end = input_string[position+length:]
            number = float(input_string[position+1:position+length])
            number = (number*(rescale_factor))
            if number<.0005: number=0
            middle = str(number)
            if '-' in middle:
                length2=7
            if '-' not in middle:
                length2=6
            for n in range(10):
                if len(middle)<length2:
                    middle=middle+'0'
            middle2 = middle[0:length2]   
            output_string = beginning+middle2+end
            return output_string
    def XY_rescale(self,input_string,rescale_factor):
        x_rescale = SampleApp.rescale_letters(self,'X',input_string,rescale_factor)
        y_rescale = SampleApp.rescale_letters(self,'Y',x_rescale,rescale_factor)
        return(y_rescale)

    def line_rescale(self,input_list,rescale_factor):
        output_list = []
        for string in input_list:
            output_string = SampleApp.XY_rescale(self,string,rescale_factor)
            output_list.append(output_string)
        return output_list
           
    def XYoffset(self,xchange,ychange,input_list):
        updated2 = []
        updated3 = []
        for p in range(len(input_list)): 
            update=SampleApp.mod_coords(self,'X',input_list[p],xchange,1)
            updated2.append(update)
            update=SampleApp.mod_coords(self,'Y',updated2[p],ychange,1)
            updated3.append(update)
        return updated3

    def Zoffset(self,zchange,input_list):
        updated = []
        for p in range(len(input_list)):
            update = SampleApp.mod_coords(self,'Z',input_list[p],zchange,1)
            updated.append(update)
        return updated


class StartPage(tk.CTkFrame):
    def __init__(self, master):
        tk.CTkFrame.__init__(self, master)

        
        self.grid_columnconfigure((0,1,2,3), weight=1)#the columns in this tuple will be equally sized
        self.grid_rowconfigure((2,4),weight=1)
        
     
        self.my_image = tk.CTkImage(light_image=Image.open("//WC-DC/Engineering/users/Intern Folder/Coby Walmsley/CNC Tag Project/Tag Pictures/Tag 1.jpg"),
                                    dark_image=Image.open("//WC-DC/Engineering/users/Intern Folder/Coby Walmsley/CNC Tag Project/Tag Pictures/Tag 1.jpg"),size=(240, 160))
        self.label=tk.CTkLabel(self,text="",image=self.my_image)
        self.label.grid(row=3, column=0, padx=10, pady=10, sticky="ew")


        self.my_image2 = tk.CTkImage(light_image=Image.open("//WC-DC/Engineering/users/Intern Folder/Coby Walmsley/CNC Tag Project/Tag Pictures/Tag 2.jpg"),
                                    dark_image=Image.open("//WC-DC/Engineering/users/Intern Folder/Coby Walmsley/CNC Tag Project/Tag Pictures/Tag 2.jpg"),size=(170, 100))
        self.label2=tk.CTkLabel(self,text="",image=self.my_image2)
        self.label2.grid(row=3, column=1, padx=10, pady=10, sticky="ew")

        self.my_image3 = tk.CTkImage(light_image=Image.open("//WC-DC/Engineering/users/Intern Folder/Coby Walmsley/CNC Tag Project/Tag Pictures/Tag 3.jpg"),
                                    dark_image=Image.open("//WC-DC/Engineering/users/Intern Folder/Coby Walmsley/CNC Tag Project/Tag Pictures/Tag 3.jpg"),size=(140, 80))
        self.label3=tk.CTkLabel(self,text="",image=self.my_image3)
        self.label3.grid(row=3, column=2, padx=10, pady=10, sticky="ew")

        self.my_image4 = tk.CTkImage(light_image=Image.open("//WC-DC/Engineering/users/Intern Folder/Coby Walmsley/CNC Tag Project/Tag Pictures/Tag 4.jpg"),
                                    dark_image=Image.open("//WC-DC/Engineering/users/Intern Folder/Coby Walmsley/CNC Tag Project/Tag Pictures/Tag 4.jpg"),size=(140, 72))
        self.label4=tk.CTkLabel(self,text="",image=self.my_image4)
        self.label4.grid(row=3, column=3, padx=10, pady=10, sticky="ew")

        self.my_image5 = tk.CTkImage(light_image=Image.open("//WC-DC/Engineering/users/Intern Folder/Coby Walmsley/CNC Tag Project/Tag Pictures/Tag 5.jpg"),
                                    dark_image=Image.open("//WC-DC/Engineering/users/Intern Folder/Coby Walmsley/CNC Tag Project/Tag Pictures/Tag 5.jpg"),size=(280, 60))
        self.label5=tk.CTkLabel(self,text="",image=self.my_image5)
        self.label5.grid(row=5, column=0, padx=10, pady=10, sticky="ew")

        self.my_image6 = tk.CTkImage(light_image=Image.open("//WC-DC/Engineering/users/Intern Folder/Coby Walmsley/CNC Tag Project/Tag Pictures/Tag 6.jpg"),
                                    dark_image=Image.open("//WC-DC/Engineering/users/Intern Folder/Coby Walmsley/CNC Tag Project/Tag Pictures/Tag 6.jpg"),size=(360, 120))
        self.label6=tk.CTkLabel(self,text="",image=self.my_image6)
        self.label6.grid(row=5, column=1, padx=10, pady=10, sticky="ew")

        self.my_image7 = tk.CTkImage(light_image=Image.open("//WC-DC/Engineering/users/Intern Folder/Coby Walmsley/CNC Tag Project/Tag Pictures/Tag 7.jpg"),
                                    dark_image=Image.open("//WC-DC/Engineering/users/Intern Folder/Coby Walmsley/CNC Tag Project/Tag Pictures/Tag 7.jpg"),size=(410, 120))
        self.label7=tk.CTkLabel(self,text="",image=self.my_image7)
        self.label7.grid(row=5, column=2, padx=10, pady=10, sticky="ew")

        self.my_image8 = tk.CTkImage(light_image=Image.open("//WC-DC/Engineering/users/Intern Folder/Coby Walmsley/CNC Tag Project/Tag Pictures/Tag 8.jpg"),
                                    dark_image=Image.open("//WC-DC/Engineering/users/Intern Folder/Coby Walmsley/CNC Tag Project/Tag Pictures/Tag 8.jpg"),size=(440, 120))
        self.label8=tk.CTkLabel(self,text="",image=self.my_image8)
        self.label8.grid(row=5, column=3, padx=10, pady=10, sticky="ew")


        self.title=tk.CTkLabel(self,text="Warren Controls Tag Engraver",font=("Roboto",28,"bold"))
        self.title.grid(row=0,column=0,padx=20,pady=20,sticky="n",columnspan=4)

        self.subtitle=tk.CTkLabel(self,text="Select Tag to Engrave",font=("Roboto",20))
        self.subtitle.grid(row=1,column=0,padx=20,pady=0,sticky="n",columnspan=4)

        self.checkbox1=tk.CTkButton(self,text="Tag 1",command=lambda: master.switch_frame(Tag1))
        self.checkbox1.grid(row=4,column=0,padx=10,pady=10,sticky="n")

        self.checkbox2=tk.CTkButton(self,text="Tag 2",command=lambda: master.switch_frame(Tag2))
        self.checkbox2.grid(row=4,column=1,padx=10,pady=10,sticky="n")

        self.checkbox3=tk.CTkButton(self,text="Tag 3",command=lambda: master.switch_frame(Tag3))
        self.checkbox3.grid(row=4,column=2,padx=10,pady=10,sticky="n")

        self.checkbox4=tk.CTkButton(self,text="Tag 4",command=lambda: master.switch_frame(Tag4))
        self.checkbox4.grid(row=4,column=3,padx=10,pady=10,sticky="n")

        self.checkbox5=tk.CTkButton(self,text="Tag 5",command=lambda: master.switch_frame(Tag5))
        self.checkbox5.grid(row=6,column=0,padx=10,pady=10,sticky="n")

        self.checkbox6=tk.CTkButton(self,text="Tag 6",command=lambda: master.switch_frame(Tag6))
        self.checkbox6.grid(row=6,column=1,padx=10,pady=10,sticky="n")

        self.checkbox7=tk.CTkButton(self,text="Tag 7",command=lambda: master.switch_frame(Tag7))
        self.checkbox7.grid(row=6,column=2,padx=10,pady=10,sticky="n")

        self.checkbox8=tk.CTkButton(self,text="Tag 8",command=lambda: master.switch_frame(Tag8))
        self.checkbox8.grid(row=6,column=3,padx=10,pady=10,sticky="n")

class Tag1(tk.CTkFrame):
    def __init__(self, master):
        tk.CTkFrame.__init__(self, master)
        self.grid_columnconfigure((0,1,2,3), weight=1)
        self.title=tk.CTkLabel(self,text="Tag 1",font=("Roboto",28,"bold"))  ##Change Tag title
        self.title.grid(row=0,column=3,padx=20,pady=20,sticky="n",columnspan=3)

        self.subtitle=tk.CTkLabel(self,text="Enter Engraving Information",font=("Roboto",20))
        self.subtitle.grid(row=1,column=3,padx=20,pady=0,sticky="n",columnspan=3)
        
        self.my_image = tk.CTkImage(light_image=Image.open("//WC-DC/Engineering/users/Intern Folder/Coby Walmsley/CNC Tag Project/Tag Pictures/Tag 1.jpg"),
                                    dark_image=Image.open("//WC-DC/Engineering/users/Intern Folder/Coby Walmsley/CNC Tag Project/Tag Pictures/Tag 1.jpg"),size=(480, 320))
        self.label=tk.CTkLabel(self,text="",image=self.my_image)
        self.label.grid(row=3, column=3, padx=10, pady=10, sticky="n",columnspan=3)


        tk.CTkButton(self, text="Back",
                  command=lambda: master.switch_frame(StartPage)).grid(row=6,column=3,padx=20,pady=20)
        tk.CTkButton(self, text="Write Gcode",command=self.write1).grid(row=5,column=3,padx=20,pady=20)

        self.label1=tk.CTkLabel(self,text="SERIAL NO.").grid(row=4,column=5,sticky='sew')
        self.entry1 = tk.CTkEntry(self, placeholder_text="12 character limit")
        self.entry1.grid(row=5,column=5,padx=30,pady=20,sticky="new")
        self.label2=tk.CTkLabel(self,text="CID").grid(row=6,column=5,sticky='sew')

        self.entry2 = tk.CTkEntry(self, placeholder_text="8 character limit")
        self.entry2.grid(row=7,column=5,padx=30,pady=20,sticky="ew")

        self.label3=tk.CTkLabel(self,text="CD").grid(row=4,column=6,sticky='sew')
        self.entry3 = tk.CTkEntry(self, placeholder_text="8 character limit")
        self.entry3.grid(row=5,column=6,padx=30,pady=20,sticky="new")
        self.label4=tk.CTkLabel(self,text="SET PRESS RNG (PSIG)").grid(row=6,column=6,sticky='sew')
        self.entry4 = tk.CTkEntry(self, placeholder_text="8 character limit")
        self.entry4.grid(row=7,column=6,padx=30,pady=20,sticky="new")

        self.label5=tk.CTkLabel(self,text="ASTM F 1370").grid(row=6,column=7,sticky='sew')
        self.entry5 = tk.CTkEntry(self, placeholder_text="5 character limit")
        self.entry5.grid(row=7,column=7,padx=30,pady=20,sticky="new")

    def collect_letters1(self,save_file,info,letter_folder_path,possible_chars):
        print("Collecting Letters")
        full_program=[]
        shifted_program=[]
        full_program.append('G90\n')
        full_program.append('G20\n')
        full_program.append('G17 G64 P0.001 M3 S10000\n')
        full_program.append('F20.00\n')
        total_info = []
        for n in info:
            total_info.append(n)
        rescale_factor = 1
        x_shift = 0
        y_shift = 0
        z_shift = .0003
        
        
        
        for t in range(len(total_info)):
            letter_data = []
            for n in total_info[t]:
                
                if n.isalpha():
                    n = n.capitalize()
                if n not in possible_chars:
                    n = '#'
                var = n
                if n=='/':
                    var = 'SLASH'
                if n=='.':
                    var = 'PERIOD'
                if n==':':
                    var = 'COLON'
                if n==' ':
                    var = 'SPACE'
                path = letter_folder_path + '/' + f'{var}.txt'
                f = open(path,'r')
                lines = f.readlines()
           
                letter_data.append(lines)
                f.close()
            print('created letter data')
            updated = []
            coordinate=0
            for letternum in letter_data:
                if t!=4:    
                    for p in range(len(letternum)):
                        update=SampleApp.mod_coords(self,'X',letternum[p],.125,coordinate)
                        if '\n' not in update:
                            update = update+'\n'
                        updated.append(update)
                if t==4:
                    for p in range(len(letternum)):
                        update=SampleApp.mod_coords(self,'X',letternum[p],.16,coordinate)
                        if '\n' not in update:
                            update = update+'\n'
                        updated.append(update)
                coordinate+=1
            print("created spaces")
            if t==0:
                offset =updated
                print("Completed first box")
            if t==1:
                offset = SampleApp.XYoffset(self,-.68,-.225,updated)
                print("completed second box")
            if t==2:
                offset = SampleApp.XYoffset(self,.62,-.225,updated)
                print("completed third box")
            if t==3:
                offset = SampleApp.XYoffset(self,.5,-.45,updated)
                print("completed fourth box")
            if t==4:
                offset = SampleApp.XYoffset(self,.62,-.73,updated)
                print("completed fifth box")
            for line in offset:
                shifted_program.append(line)
            print("boxes combined")
            shifted_program2 = SampleApp.XYoffset(self,x_shift,y_shift,shifted_program)
            print('origin shifted')
        z_shifted = SampleApp.Zoffset(self,z_shift,shifted_program2)
        print("z shifted")
        full_program = full_program+z_shifted
        print("program done")
        print("z shifted")
        full_program = full_program+z_shifted
        print("program done")
            
        full_program.append("G0 Z1.500\n")
        full_program.append("G0 X0.000 Y0.000\n")
        full_program.append('M5\n')
        full_program.append('M2\n')
        f = open(f'{save_file}.txt','w')
        for line in full_program:
            f.write(line)
        f.close()


    def write1(self):
        folder_path="//WC-DC/Engineering/users/Intern Folder/Coby Walmsley/CNC Tag Project/.15 Inch Letters"
        available_chars=['!','#',"A","B",'C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','1','2','3','4','5','6','7','8','9','0','.','/','%',':',';','&','(',')',',','-','+','=',' ']
        data_list=[]
        data_list.append(self.entry1.get())
        data_list.append(self.entry3.get())
        data_list.append(self.entry2.get())
        data_list.append(self.entry4.get())
        data_list.append(self.entry5.get())
        if len(data_list[0])<13:
            print('good 1/5')
            if len(data_list[1])<9:
                print('good 2/5')
                if len(data_list[2])<9:
                    print('good 3/5')
                    if len(data_list[3])<9:
                        print('good 4/5')
                        if len(data_list[4])<6:
                            print('good 5/5')
                            self.collect_letters1("Tag Engraving",data_list,folder_path,available_chars)
        print(data_list)

class Tag2(tk.CTkFrame):
    def __init__(self, master):
        tk.CTkFrame.__init__(self, master)
        self.grid_columnconfigure((0,1,2,3), weight=1)
        self.title=tk.CTkLabel(self,text="Tag 2",font=("Roboto",28,"bold"))  ##Change Tag title
        self.title.grid(row=0,column=3,padx=20,pady=20,sticky="n",columnspan=3)

        self.subtitle=tk.CTkLabel(self,text="Enter Engraving Information",font=("Roboto",20))
        self.subtitle.grid(row=1,column=3,padx=20,pady=0,sticky="n",columnspan=3)
        
        self.my_image = tk.CTkImage(light_image=Image.open("//WC-DC/Engineering/users/Intern Folder/Coby Walmsley/CNC Tag Project/Tag Pictures/Tag 2.jpg"),
                                    dark_image=Image.open("//WC-DC/Engineering/users/Intern Folder/Coby Walmsley/CNC Tag Project/Tag Pictures/Tag 2.jpg"),size=(340, 200))
        self.label=tk.CTkLabel(self,text="",image=self.my_image)
        self.label.grid(row=3, column=3, padx=10, pady=10, sticky="n",columnspan=3)


        tk.CTkButton(self, text="Back",
                  command=lambda: master.switch_frame(StartPage)).grid(row=6,column=3,padx=20,pady=20)
        tk.CTkButton(self, text="Write Gcode",command=self.write2).grid(row=5,column=3,padx=20,pady=20)

        self.label1=tk.CTkLabel(self,text="CID").grid(row=4,column=5,sticky='sew')
        self.entry1 = tk.CTkEntry(self, placeholder_text="8 character limit")
        self.entry1.grid(row=5,column=5,padx=30,pady=20,sticky="new")
        self.label2=tk.CTkLabel(self,text="CONNECTIONS").grid(row=4,column=6,sticky='sew')

        self.entry2 = tk.CTkEntry(self, placeholder_text="6 character limit")
        self.entry2.grid(row=5,column=6,padx=30,pady=20,sticky="ew")

        self.label3=tk.CTkLabel(self,text="SERIAL NO.").grid(row=6,column=5,sticky='sew')
        self.entry3 = tk.CTkEntry(self, placeholder_text="7 character limit")
        self.entry3.grid(row=7,column=5,padx=30,pady=20,sticky="new")
        

    def collect_letters2(self,save_file,info,letter_folder_path,possible_chars):
        print("Collecting Letters")
        full_program=[]
        shifted_program=[]
        full_program.append('G90\n')
        full_program.append('G20\n')
        full_program.append('G17 G64 P0.001 M3 S10000\n')
        full_program.append('F20.00\n')
        total_info = []
        for n in info:
            total_info.append(n) 
        
        rescale_factor = .8
        x_shift = 0
        y_shift = 0
        z_shift = .0006
 
        print("creating letters")
        for t in range(len(total_info)):
            letter_data = []
            for n in total_info[t]:
                
                if n.isalpha():
                    n = n.capitalize()
                if n not in possible_chars:
                    n = '#'
                var = n
                if n=='/':
                    var = 'SLASH'
                if n=='.':
                    var = 'PERIOD'
                if n==':':
                    var = 'COLON'
                if n==' ':
                    var = 'SPACE'
                path = letter_folder_path + '/' + f'{var}.txt'
                f = open(path,'r')
                lines = f.readlines()
           
                letter_data.append(lines)
                f.close()
            print("created letters") 
            updated = []
            coordinate=0
            print("creating spaces")
            for letternum in letter_data:
                for p in range(len(letternum)):
                    update=SampleApp.mod_coords(self,'X',letternum[p],.125,coordinate)
                    if '\n' not in update:
                        update = update+'\n'
                    updated.append(update)
                coordinate+=1
            print("creating spaces")
            updated2 = SampleApp.line_rescale(self,updated,rescale_factor)
            print("rescale complete")
            if t==0: 
                offset =updated2
            if t==1:
                offset = SampleApp.XYoffset(self,.491,-.255,updated2)
            if t==2:
                offset = SampleApp.XYoffset(self,.38,-.48,updated2)
            print("boxes complete")
            for line in offset:
                shifted_program.append(line)
            print("boxes combined")
            shifted_program2 = SampleApp.XYoffset(self,x_shift,y_shift,shifted_program)
            print('origin shifted')
        z_shifted = SampleApp.Zoffset(self,z_shift,shifted_program2)
        print("z shifted")
        full_program = full_program+z_shifted
        print("program done")
        
            
        full_program.append("G0 Z1.500\n")
        full_program.append("G0 X0.000 Y0.000\n")
        full_program.append('M5\n')
        full_program.append('M2\n')
        f = open(f'{save_file}.txt','w')
        for line in full_program:
            f.write(line)
        f.close()


    def write2(self):
        folder_path="//WC-DC/Engineering/users/Intern Folder/Coby Walmsley/CNC Tag Project/.15 Inch Letters"
        available_chars=['!','#',"A","B",'C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','1','2','3','4','5','6','7','8','9','0','.','/','%',':',';','&','(',')',',','-','+','=',' ']
        data_list=[]
        data_list.append(self.entry1.get())
        data_list.append(self.entry2.get())
        data_list.append(self.entry3.get())
        if len(data_list[0])<9:
            print('good 1/3')
            if len(data_list[1])<7:
                print('good 2/3')
                if len(data_list[2])<8:
                    print('good 3/3')
                    self.collect_letters2("Tag Engraving",data_list,folder_path,available_chars)
        

        
        
class Tag3(tk.CTkFrame):
    def __init__(self, master):
        tk.CTkFrame.__init__(self, master)
        self.grid_columnconfigure((0,1,2,3), weight=1)
        self.title=tk.CTkLabel(self,text="Tag 3",font=("Roboto",28,"bold"))  ##Change Tag title
        self.title.grid(row=0,column=3,padx=20,pady=20,sticky="n",columnspan=3)

        self.subtitle=tk.CTkLabel(self,text="Enter Engraving Information",font=("Roboto",20))
        self.subtitle.grid(row=1,column=3,padx=20,pady=0,sticky="n",columnspan=3)
        
        self.my_image = tk.CTkImage(light_image=Image.open("//WC-DC/Engineering/users/Intern Folder/Coby Walmsley/CNC Tag Project/Tag Pictures/Tag 3.jpg"),
                                    dark_image=Image.open("//WC-DC/Engineering/users/Intern Folder/Coby Walmsley/CNC Tag Project/Tag Pictures/Tag 3.jpg"),size=(280, 160))
        self.label=tk.CTkLabel(self,text="",image=self.my_image)
        self.label.grid(row=3, column=3, padx=10, pady=10, sticky="n",columnspan=3)


        tk.CTkButton(self, text="Back",
                  command=lambda: master.switch_frame(StartPage)).grid(row=6,column=3,padx=20,pady=20)
        tk.CTkButton(self, text="Write Gcode",command=self.write2).grid(row=5,column=3,padx=20,pady=20)

        self.label1=tk.CTkLabel(self,text="Cv").grid(row=4,column=5,sticky='sew')
        self.entry1 = tk.CTkEntry(self, placeholder_text="5 character limit")
        self.entry1.grid(row=5,column=5,padx=30,pady=20,sticky="new")
        self.label2=tk.CTkLabel(self,text="Tmax").grid(row=4,column=6,sticky='sew')

        self.entry2 = tk.CTkEntry(self, placeholder_text="5 character limit")
        self.entry2.grid(row=5,column=6,padx=30,pady=20,sticky="ew")
        

    def collect_letters2(self,save_file,info,letter_folder_path,possible_chars):
        print("Collecting Letters")
        full_program=[]
        shifted_program=[]
        full_program.append('G90\n')
        full_program.append('G20\n')
        full_program.append('G17 G64 P0.001 M3 S10000\n')
        full_program.append('F20.00\n')
        total_info = []
        for n in info:
            total_info.append(n) 
        
        rescale_factor = .8
        x_shift = 0
        y_shift = 0
        z_shift = .0006
 
        print("creating letters")
        for t in range(len(total_info)):
            letter_data = []
            for n in total_info[t]:
                
                if n.isalpha():
                    n = n.capitalize()
                if n not in possible_chars:
                    n = '#'
                var = n
                if n=='/':
                    var = 'SLASH'
                if n=='.':
                    var = 'PERIOD'
                if n==':':
                    var = 'COLON'
                if n==' ':
                    var = 'SPACE'
                path = letter_folder_path + '/' + f'{var}.txt'
                f = open(path,'r')
                lines = f.readlines()
           
                letter_data.append(lines)
                f.close()
            print("created letters") 
            updated = []
            coordinate=0
            print("creating spaces")
            for letternum in letter_data:
                for p in range(len(letternum)):
                    update=SampleApp.mod_coords(self,'X',letternum[p],.125,coordinate)
                    if '\n' not in update:
                        update = update+'\n'
                    updated.append(update)
                coordinate+=1
            print("creating spaces")
            updated2 = SampleApp.line_rescale(self,updated,rescale_factor)
            print("rescale complete")
            if t==0: 
                offset =updated2
            if t==1:
                offset = SampleApp.XYoffset(self,.87,0,updated2) 
            print("boxes complete")
            for line in offset:
                shifted_program.append(line)
            print("boxes combined")
            shifted_program2 = SampleApp.XYoffset(self,x_shift,y_shift,shifted_program)
            print('origin shifted')
        z_shifted = SampleApp.Zoffset(self,z_shift,shifted_program2)
        print("z shifted")
        full_program = full_program+z_shifted
        print("program done")
            
        full_program.append("G0 Z1.500\n")
        full_program.append("G0 X0.000 Y0.000\n")
        full_program.append('M5\n')
        full_program.append('M2\n')
        f = open(f'{save_file}.txt','w')
        for line in full_program:
            f.write(line)
        f.close()

    def write2(self):
        folder_path="//WC-DC/Engineering/users/Intern Folder/Coby Walmsley/CNC Tag Project/.15 Inch Letters"
        available_chars=['!','#',"A","B",'C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','1','2','3','4','5','6','7','8','9','0','.','/','%',':',';','&','(',')',',','-','+','=',' ']
        data_list=[]
        data_list.append(self.entry1.get())
        data_list.append(self.entry2.get())
        if len(data_list[0])<6:
            print('good 1/2')
            if len(data_list[1])<6:
                print('good 2/2')
                self.collect_letters2("Tag Engraving",data_list,folder_path,available_chars)    
        
        
class Tag4(tk.CTkFrame):
    def __init__(self, master):
        tk.CTkFrame.__init__(self, master)
        self.grid_columnconfigure((0,1,2,3), weight=1)
        self.title=tk.CTkLabel(self,text="Tag 4",font=("Roboto",28,"bold"))  ##Change Tag title
        self.title.grid(row=0,column=3,padx=20,pady=20,sticky="n",columnspan=3)

        self.subtitle=tk.CTkLabel(self,text="Enter Engraving Information",font=("Roboto",20))
        self.subtitle.grid(row=1,column=3,padx=20,pady=0,sticky="n",columnspan=3)
        
        self.my_image = tk.CTkImage(light_image=Image.open("//WC-DC/Engineering/users/Intern Folder/Coby Walmsley/CNC Tag Project/Tag Pictures/Tag 4.jpg"),
                                    dark_image=Image.open("//WC-DC/Engineering/users/Intern Folder/Coby Walmsley/CNC Tag Project/Tag Pictures/Tag 4.jpg"),size=(280, 144))
        self.label=tk.CTkLabel(self,text="",image=self.my_image)
        self.label.grid(row=3, column=3, padx=10, pady=10, sticky="n",columnspan=3)


        tk.CTkButton(self, text="Back",
                  command=lambda: master.switch_frame(StartPage)).grid(row=6,column=3,padx=20,pady=20)
        tk.CTkButton(self, text="Write Gcode",command=self.write2).grid(row=5,column=3,padx=20,pady=20)

        self.label1=tk.CTkLabel(self,text="Cv").grid(row=4,column=5,sticky='sew')
        self.entry1 = tk.CTkEntry(self, placeholder_text="5 character limit")
        self.entry1.grid(row=5,column=5,padx=30,pady=20,sticky="new")

        self.label2=tk.CTkLabel(self,text="Tmax").grid(row=4,column=6,sticky='sew')
        self.entry2 = tk.CTkEntry(self, placeholder_text="5 character limit")
        self.entry2.grid(row=5,column=6,padx=30,pady=20,sticky="ew")

        self.label3=tk.CTkLabel(self,text="CHAR").grid(row=6,column=5,sticky='sew')
        self.entry3 = tk.CTkEntry(self, placeholder_text="5 character limit")
        self.entry3.grid(row=7,column=5,padx=30,pady=20,sticky="ew")

        self.label4=tk.CTkLabel(self,text="TRIM MATL").grid(row=6,column=6,sticky='sew')
        self.entry4 = tk.CTkEntry(self, placeholder_text="5 character limit")
        self.entry4.grid(row=7,column=6,padx=30,pady=20,sticky="ew")
        

    def collect_letters2(self,save_file,info,letter_folder_path,possible_chars):
        print("Collecting Letters")
        full_program=[]
        shifted_program=[]
        full_program.append('G90\n')
        full_program.append('G20\n')
        full_program.append('G17 G64 P0.001 M3 S10000\n')
        full_program.append('F20.00\n')
        total_info = []
        for n in info:
            total_info.append(n) 
        
        rescale_factor = .8
        x_shift = 0
        y_shift = 0
        z_shift = .0006
 
        print("creating letters")
        for t in range(len(total_info)):
            letter_data = []
            for n in total_info[t]:
                
                if n.isalpha():
                    n = n.capitalize()
                if n not in possible_chars:
                    n = '#'
                var = n
                if n=='/':
                    var = 'SLASH'
                if n=='.':
                    var = 'PERIOD'
                if n==':':
                    var = 'COLON'
                if n==' ':
                    var = 'SPACE'
                path = letter_folder_path + '/' + f'{var}.txt'
                f = open(path,'r')
                lines = f.readlines()
           
                letter_data.append(lines)
                f.close()
            print("created letters") 
            updated = []
            coordinate=0
            print("creating spaces")
            for letternum in letter_data:
                for p in range(len(letternum)):
                    update=SampleApp.mod_coords(self,'X',letternum[p],.125,coordinate)
                    if '\n' not in update:
                        update = update+'\n'
                    updated.append(update)
                coordinate+=1
            print("creating spaces")
            updated2 = SampleApp.line_rescale(self,updated,rescale_factor)
            print("rescale complete")
            if t==0: 
                offset =updated2
            if t==1:
                offset = SampleApp.XYoffset(self,.87,0,updated2)
            if t==2:
                offset = SampleApp.XYoffset(self,.41,-.25,updated2)
            if t==3:
                offset = SampleApp.XYoffset(self,.86,-.46,updated2)
            print("boxes complete")
            for line in offset:
                shifted_program.append(line)
            print("boxes combined")
            shifted_program2 = SampleApp.XYoffset(self,x_shift,y_shift,shifted_program)
            print('origin shifted')
        z_shifted = SampleApp.Zoffset(self,z_shift,shifted_program2)
        print("z shifted")
        full_program = full_program+z_shifted
        print("program done")
            
        full_program.append("G0 Z1.500\n")
        full_program.append("G0 X0.000 Y0.000\n")
        full_program.append('M5\n')
        full_program.append('M2\n')
        f = open(f'{save_file}.txt','w')
        for line in full_program:
            f.write(line)
        f.close()

    def write2(self):
        folder_path="//WC-DC/Engineering/users/Intern Folder/Coby Walmsley/CNC Tag Project/.15 Inch Letters"
        available_chars=['!','#',"A","B",'C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','1','2','3','4','5','6','7','8','9','0','.','/','%',':',';','&','(',')',',','-','+','=',' ']
        data_list=[]
        data_list.append(self.entry1.get())
        data_list.append(self.entry2.get())
        if len(data_list[0])<6:
            print('good 1/2')
            if len(data_list[1])<6:
                print('good 2/2')
                if len(data_list[2])<6:
                    print('good 2/2')
                    if len(data_list[3])<6:
                        print('good 2/2')
                self.collect_letters2("Tag Engraving",data_list,folder_path,available_chars)

class Tag5(tk.CTkFrame):
    def __init__(self, master):
        tk.CTkFrame.__init__(self, master)
        self.grid_columnconfigure((0,1,2,3), weight=1)
        self.title=tk.CTkLabel(self,text="Tag 5",font=("Roboto",28,"bold"))  ##Change Tag title
        self.title.grid(row=0,column=3,padx=20,pady=20,sticky="n",columnspan=3)

        self.subtitle=tk.CTkLabel(self,text="Enter Engraving Information",font=("Roboto",20))
        self.subtitle.grid(row=1,column=3,padx=20,pady=0,sticky="n",columnspan=3)
        
        self.my_image = tk.CTkImage(light_image=Image.open("//WC-DC/Engineering/users/Intern Folder/Coby Walmsley/CNC Tag Project/Tag Pictures/Tag 5.jpg"),
                                    dark_image=Image.open("//WC-DC/Engineering/users/Intern Folder/Coby Walmsley/CNC Tag Project/Tag Pictures/Tag 5.jpg"),size=(560, 120))
        self.label=tk.CTkLabel(self,text="",image=self.my_image)
        self.label.grid(row=3, column=3, padx=10, pady=10, sticky="n",columnspan=3)


        tk.CTkButton(self, text="Back",
                  command=lambda: master.switch_frame(StartPage)).grid(row=6,column=3,padx=20,pady=20)
        tk.CTkButton(self, text="Write Gcode",command=self.write2).grid(row=5,column=3,padx=20,pady=20)

        self.label1=tk.CTkLabel(self,text="Inscription").grid(row=4,column=5,sticky='sew')
        self.entry1 = tk.CTkEntry(self, placeholder_text="12 character limit")
        self.entry1.grid(row=5,column=5,padx=30,pady=20,sticky="new")

    def collect_letters2(self,save_file,info,letter_folder_path,possible_chars):
        print("Collecting Letters")
        full_program=[]
        shifted_program=[]
        full_program.append('G90\n')
        full_program.append('G20\n')
        full_program.append('G17 G64 P0.001 M3 S10000\n')
        full_program.append('F20.00\n')
        total_info = []
        for n in info:
            total_info.append(n) 
        
        rescale_factor = 1.25
        x_shift = 0
        y_shift = 0
        z_shift = .0006
 
        print("creating letters")
        for t in range(len(total_info)):
            letter_data = []
            for n in total_info[t]:
                
                if n.isalpha():
                    n = n.capitalize()
                if n not in possible_chars:
                    n = '#'
                var = n
                if n=='/':
                    var = 'SLASH'
                if n=='.':
                    var = 'PERIOD'
                if n==':':
                    var = 'COLON'
                if n==' ':
                    var = 'SPACE'
                path = letter_folder_path + '/' + f'{var}.txt'
                f = open(path,'r')
                lines = f.readlines()
           
                letter_data.append(lines)
                f.close()
            print("created letters") 
            updated = []
            coordinate=0
            print("creating spaces")
            for letternum in letter_data:
                for p in range(len(letternum)):
                    update=SampleApp.mod_coords(self,'X',letternum[p],.125,coordinate)
                    if '\n' not in update:
                        update = update+'\n'
                    updated.append(update)
                coordinate+=1
            print("creating spaces")
            updated2 = SampleApp.line_rescale(self,updated,rescale_factor)
            print("rescale complete")
            if t==0: 
                offset =updated2
            print("boxes complete")
            for line in offset:
                shifted_program.append(line)
            print("boxes combined")
            shifted_program2 = SampleApp.XYoffset(self,x_shift,y_shift,shifted_program)
            print('origin shifted')
        z_shifted = SampleApp.Zoffset(self,z_shift,shifted_program2)
        print("z shifted")
        full_program = full_program+z_shifted
        print("program done")
            
        full_program.append("G0 Z1.500\n")
        full_program.append("G0 X0.000 Y0.000\n")
        full_program.append('M5\n')
        full_program.append('M2\n')
        f = open(f'{save_file}.txt','w')
        for line in full_program:
            f.write(line)
        f.close()

    def write2(self):
        folder_path="//WC-DC/Engineering/users/Intern Folder/Coby Walmsley/CNC Tag Project/.15 Inch Letters"
        available_chars=['!','#',"A","B",'C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','1','2','3','4','5','6','7','8','9','0','.','/','%',':',';','&','(',')',',','-','+','=',' ']
        data_list=[]
        data_list.append(self.entry1.get())
        data_list.append(self.entry2.get())
        if len(data_list[0])<13:
            print('good 1/1')
            self.collect_letters2("App_Trial2.txt",data_list,folder_path,available_chars)

class Tag6(tk.CTkFrame):
    def __init__(self, master):
        tk.CTkFrame.__init__(self, master)
        self.grid_columnconfigure((0,1,2,3), weight=1)
        self.title=tk.CTkLabel(self,text="Tag 6",font=("Roboto",28,"bold"))  ##Change Tag title
        self.title.grid(row=0,column=3,padx=20,pady=20,sticky="n",columnspan=3)

        self.subtitle=tk.CTkLabel(self,text="Enter Engraving Information",font=("Roboto",20))
        self.subtitle.grid(row=1,column=3,padx=20,pady=0,sticky="n",columnspan=3)
        
        self.my_image = tk.CTkImage(light_image=Image.open("//WC-DC/Engineering/users/Intern Folder/Coby Walmsley/CNC Tag Project/Tag Pictures/Tag 6.jpg"),
                                    dark_image=Image.open("//WC-DC/Engineering/users/Intern Folder/Coby Walmsley/CNC Tag Project/Tag Pictures/Tag 6.jpg"),size=(720, 240))
        self.label=tk.CTkLabel(self,text="",image=self.my_image)
        self.label.grid(row=3, column=3, padx=10, pady=10, sticky="n",columnspan=3)


        tk.CTkButton(self, text="Back",
                  command=lambda: master.switch_frame(StartPage)).grid(row=6,column=3,padx=20,pady=20)
        tk.CTkButton(self, text="Write Gcode",command=self.write2).grid(row=5,column=3,padx=20,pady=20)

        self.label1=tk.CTkLabel(self,text="SIG").grid(row=4,column=5,sticky='sew')
        self.entry1 = tk.CTkEntry(self, placeholder_text="9 character limit")
        self.entry1.grid(row=5,column=5,padx=30,pady=20,sticky="new")

        self.label2=tk.CTkLabel(self,text="Tmax").grid(row=4,column=6,sticky='sew')
        self.entry2 = tk.CTkEntry(self, placeholder_text="9 character limit")
        self.entry2.grid(row=5,column=6,padx=30,pady=20,sticky="ew")

        self.label3=tk.CTkLabel(self,text="SUP").grid(row=6,column=5,sticky='sew')
        self.entry3 = tk.CTkEntry(self, placeholder_text="9 character limit")
        self.entry3.grid(row=7,column=5,padx=30,pady=20,sticky="ew")

        self.label4=tk.CTkLabel(self,text="S/N").grid(row=6,column=6,sticky='sew')
        self.entry4 = tk.CTkEntry(self, placeholder_text="9 character limit")
        self.entry4.grid(row=7,column=6,padx=30,pady=20,sticky="ew")

        self.label5=tk.CTkLabel(self,text="P/N").grid(row=8,column=5,sticky='sew')
        self.entry5 = tk.CTkEntry(self, placeholder_text="12 character limit")
        self.entry5.grid(row=9,column=5,padx=30,pady=20,sticky="ew")
        

    def collect_letters2(self,save_file,info,letter_folder_path,possible_chars):
        print("Collecting Letters")
        full_program=[]
        shifted_program=[]
        full_program.append('G90\n')
        full_program.append('G20\n')
        full_program.append('G17 G64 P0.001 M3 S10000\n')
        full_program.append('F20.00\n')
        total_info = []
        for n in info:
            total_info.append(n) 
        
        rescale_factor = .8
        x_shift = 0
        y_shift = 0
        z_shift = .0006
 
        print("creating letters")
        for t in range(len(total_info)):
            letter_data = []
            for n in total_info[t]:
                
                if n.isalpha():
                    n = n.capitalize()
                if n not in possible_chars:
                    n = '#'
                var = n
                if n=='/':
                    var = 'SLASH'
                if n=='.':
                    var = 'PERIOD'
                if n==':':
                    var = 'COLON'
                if n==' ':
                    var = 'SPACE'
                path = letter_folder_path + '/' + f'{var}.txt'
                f = open(path,'r')
                lines = f.readlines()
           
                letter_data.append(lines)
                f.close()
            print("created letters") 
            updated = []
            coordinate=0
            print("creating spaces")
            for letternum in letter_data:
                for p in range(len(letternum)):
                    update=SampleApp.mod_coords(self,'X',letternum[p],.125,coordinate)
                    if '\n' not in update:
                        update = update+'\n'
                    updated.append(update)
                coordinate+=1
            print("creating spaces")
            updated2 = SampleApp.line_rescale(self,updated,rescale_factor)
            print("rescale complete")
            if t==0: 
                offset =updated2
            if t==1:
                offset = SampleApp.XYoffset(self,0,-.32,updated2)
            if t==2:
                offset = SampleApp.XYoffset(self,0,-.64,updated2)
            if t==3:
                offset = SampleApp.XYoffset(self,2.39,.125,updated2)
            if t==4:
                offset = SampleApp.XYoffset(self,2.39,-.32,updated2)
            print("boxes complete")
            for line in offset:
                shifted_program.append(line)
            print("boxes combined")
            shifted_program2 = SampleApp.XYoffset(self,x_shift,y_shift,shifted_program)
            print('origin shifted')
        z_shifted = SampleApp.Zoffset(self,z_shift,shifted_program2)
        print("z shifted")
        full_program = full_program+z_shifted
        print("program done")
            
        full_program.append("G0 Z1.500\n")
        full_program.append("G0 X0.000 Y0.000\n")
        full_program.append('M5\n')
        full_program.append('M2\n')
        f = open(f'{save_file}.txt','w')
        for line in full_program:
            f.write(line)
        f.close()

    def write2(self):
        folder_path="//WC-DC/Engineering/users/Intern Folder/Coby Walmsley/CNC Tag Project/.15 Inch Letters"
        available_chars=['!','#',"A","B",'C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','1','2','3','4','5','6','7','8','9','0','.','/','%',':',';','&','(',')',',','-','+','=',' ']
        data_list=[]
        data_list.append(self.entry1.get())
        data_list.append(self.entry2.get())
        if len(data_list[0])<10:
            print('good 1/5')
            if len(data_list[1])<10:
                print('good 2/5')
                if len(data_list[2])<10:
                    print('good 3/5')
                    if len(data_list[3])<10:
                        print('good 4/5')
                        if len(data_list[4])<12:
                            print('good 5/5')
                            self.collect_letters2("Tag Engraving",data_list,folder_path,available_chars)

class Tag7(tk.CTkFrame):
    def __init__(self, master):
        tk.CTkFrame.__init__(self, master)
        self.grid_columnconfigure((0,1,2,3), weight=1)
        self.title=tk.CTkLabel(self,text="Tag 7",font=("Roboto",28,"bold"))  ##Change Tag title
        self.title.grid(row=0,column=3,padx=20,pady=20,sticky="n",columnspan=3)

        self.subtitle=tk.CTkLabel(self,text="Enter Engraving Information",font=("Roboto",20))
        self.subtitle.grid(row=1,column=3,padx=20,pady=0,sticky="n",columnspan=3)
        
        self.my_image = tk.CTkImage(light_image=Image.open("//WC-DC/Engineering/users/Intern Folder/Coby Walmsley/CNC Tag Project/Tag Pictures/Tag 7.jpg"),
                                    dark_image=Image.open("//WC-DC/Engineering/users/Intern Folder/Coby Walmsley/CNC Tag Project/Tag Pictures/Tag 7.jpg"),size=(820, 240))
        self.label=tk.CTkLabel(self,text="",image=self.my_image)
        self.label.grid(row=3, column=3, padx=10, pady=10, sticky="n",columnspan=3)


        tk.CTkButton(self, text="Back",
                  command=lambda: master.switch_frame(StartPage)).grid(row=6,column=3,padx=20,pady=20)
        tk.CTkButton(self, text="Write Gcode",command=self.write2).grid(row=5,column=3,padx=20,pady=20)

        self.label1=tk.CTkLabel(self,text="SUPPLY").grid(row=4,column=5,sticky='sew')
        self.entry1 = tk.CTkEntry(self, placeholder_text="9 character limit")
        self.entry1.grid(row=5,column=5,padx=30,pady=20,sticky="new")

        self.label2=tk.CTkLabel(self,text="TMAX").grid(row=4,column=6,sticky='sew')
        self.entry2 = tk.CTkEntry(self, placeholder_text="9 character limit")
        self.entry2.grid(row=5,column=6,padx=30,pady=20,sticky="ew")

        self.label3=tk.CTkLabel(self,text="SIG").grid(row=6,column=5,sticky='sew')
        self.entry3 = tk.CTkEntry(self, placeholder_text="9 character limit")
        self.entry3.grid(row=7,column=5,padx=30,pady=20,sticky="ew")

        self.label4=tk.CTkLabel(self,text="S/N").grid(row=6,column=6,sticky='sew')
        self.entry4 = tk.CTkEntry(self, placeholder_text="9 character limit")
        self.entry4.grid(row=7,column=6,padx=30,pady=20,sticky="ew")

        self.label5=tk.CTkLabel(self,text="P/N").grid(row=8,column=5,sticky='sew')
        self.entry5 = tk.CTkEntry(self, placeholder_text="12 character limit")
        self.entry5.grid(row=9,column=5,padx=30,pady=20,sticky="ew")
        

    def collect_letters2(self,save_file,info,letter_folder_path,possible_chars):
        print("Collecting Letters")
        full_program=[]
        shifted_program=[]
        full_program.append('G90\n')
        full_program.append('G20\n')
        full_program.append('G17 G64 P0.001 M3 S10000\n')
        full_program.append('F20.00\n')
        total_info = []
        for n in info:
            total_info.append(n) 
        
        rescale_factor = .8
        x_shift = 0
        y_shift = 0
        z_shift = .0006
 
        print("creating letters")
        for t in range(len(total_info)):
            letter_data = []
            for n in total_info[t]:
                
                if n.isalpha():
                    n = n.capitalize()
                if n not in possible_chars:
                    n = '#'
                var = n
                if n=='/':
                    var = 'SLASH'
                if n=='.':
                    var = 'PERIOD'
                if n==':':
                    var = 'COLON'
                if n==' ':
                    var = 'SPACE'
                path = letter_folder_path + '/' + f'{var}.txt'
                f = open(path,'r')
                lines = f.readlines()
           
                letter_data.append(lines)
                f.close()
            print("created letters") 
            updated = []
            coordinate=0
            print("creating spaces")
            for letternum in letter_data:
                for p in range(len(letternum)):
                    update=SampleApp.mod_coords(self,'X',letternum[p],.125,coordinate)
                    if '\n' not in update:
                        update = update+'\n'
                    updated.append(update)
                coordinate+=1
            print("creating spaces")
            updated2 = SampleApp.line_rescale(self,updated,rescale_factor)
            print("rescale complete")
            if t==0: 
                offset =updated2
            if t==1:
                offset = SampleApp.XYoffset(self,-.38,-.31,updated2)
            if t==2:
                offset = SampleApp.XYoffset(self,-.38,-.63,updated2)
            if t==3:
                offset = SampleApp.XYoffset(self,2.73,0,updated2)
            if t==4:
                offset = SampleApp.XYoffset(self,2.73,-.31,updated2)
            print("boxes complete")
            for line in offset:
                shifted_program.append(line)
            print("boxes combined")
            shifted_program2 = SampleApp.XYoffset(self,x_shift,y_shift,shifted_program)
            print('origin shifted')
        z_shifted = SampleApp.Zoffset(self,z_shift,shifted_program2)
        print("z shifted")
        full_program = full_program+z_shifted
        print("program done")
            
        full_program.append("G0 Z1.500\n")
        full_program.append("G0 X0.000 Y0.000\n")
        full_program.append('M5\n')
        full_program.append('M2\n')
        f = open(f'{save_file}.txt','w')
        for line in full_program:
            f.write(line)
        f.close()

    def write2(self):
        folder_path="//WC-DC/Engineering/users/Intern Folder/Coby Walmsley/CNC Tag Project/.15 Inch Letters"
        available_chars=['!','#',"A","B",'C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','1','2','3','4','5','6','7','8','9','0','.','/','%',':',';','&','(',')',',','-','+','=',' ']
        data_list=[]
        data_list.append(self.entry1.get())
        data_list.append(self.entry2.get())
        if len(data_list[0])<10:
            print('good 1/5')
            if len(data_list[1])<10:
                print('good 2/5')
                if len(data_list[2])<10:
                    print('good 3/5')
                    if len(data_list[3])<10:
                        print('good 4/5')
                        if len(data_list[4])<12:
                            print('good 5/5')
                            self.collect_letters2("Tag Engraving",data_list,folder_path,available_chars)

class Tag8(tk.CTkFrame):
    def __init__(self, master):
        tk.CTkFrame.__init__(self, master)
        self.grid_columnconfigure((0,1,2,3), weight=1)
        self.title=tk.CTkLabel(self,text="Tag 8",font=("Roboto",28,"bold"))  ##Change Tag title
        self.title.grid(row=0,column=3,padx=20,pady=20,sticky="n",columnspan=3)

        self.subtitle=tk.CTkLabel(self,text="Enter Engraving Information",font=("Roboto",20))
        self.subtitle.grid(row=1,column=3,padx=20,pady=0,sticky="n",columnspan=3)
        
        self.my_image = tk.CTkImage(light_image=Image.open("//WC-DC/Engineering/users/Intern Folder/Coby Walmsley/CNC Tag Project/Tag Pictures/Tag 8.jpg"),
                                    dark_image=Image.open("//WC-DC/Engineering/users/Intern Folder/Coby Walmsley/CNC Tag Project/Tag Pictures/Tag 8.jpg"),size=(880, 240))
        self.label=tk.CTkLabel(self,text="",image=self.my_image)
        self.label.grid(row=3, column=3, padx=10, pady=10, sticky="n",columnspan=3)


        tk.CTkButton(self, text="Back",
                  command=lambda: master.switch_frame(StartPage)).grid(row=6,column=3,padx=20,pady=20)
        tk.CTkButton(self, text="Write Gcode",command=self.write2).grid(row=5,column=3,padx=20,pady=20)

        self.label1=tk.CTkLabel(self,text="SUPPLY").grid(row=4,column=5,sticky='sew')
        self.entry1 = tk.CTkEntry(self, placeholder_text="9 character limit")
        self.entry1.grid(row=5,column=5,padx=30,pady=20,sticky="new")

        self.label2=tk.CTkLabel(self,text="TMAX").grid(row=4,column=6,sticky='sew')
        self.entry2 = tk.CTkEntry(self, placeholder_text="9 character limit")
        self.entry2.grid(row=5,column=6,padx=30,pady=20,sticky="ew")

        self.label3=tk.CTkLabel(self,text="SIG").grid(row=6,column=5,sticky='sew')
        self.entry3 = tk.CTkEntry(self, placeholder_text="9 character limit")
        self.entry3.grid(row=7,column=5,padx=30,pady=20,sticky="ew")

        self.label4=tk.CTkLabel(self,text="S/N").grid(row=6,column=6,sticky='sew')
        self.entry4 = tk.CTkEntry(self, placeholder_text="9 character limit")
        self.entry4.grid(row=7,column=6,padx=30,pady=20,sticky="ew")

        self.label5=tk.CTkLabel(self,text="P/N").grid(row=8,column=5,sticky='sew')
        self.entry5 = tk.CTkEntry(self, placeholder_text="12 character limit")
        self.entry5.grid(row=9,column=5,padx=30,pady=20,sticky="ew")
        

    def collect_letters2(self,save_file,info,letter_folder_path,possible_chars):
        print("Collecting Letters")
        full_program=[]
        shifted_program=[]
        full_program.append('G90\n')
        full_program.append('G20\n')
        full_program.append('G17 G64 P0.001 M3 S10000\n')
        full_program.append('F20.00\n')
        total_info = []
        for n in info:
            total_info.append(n) 
        
        rescale_factor = .8
        x_shift = 0
        y_shift = 0
        z_shift = .0006
 
        print("creating letters")
        for t in range(len(total_info)):
            letter_data = []
            for n in total_info[t]:
                
                if n.isalpha():
                    n = n.capitalize()
                if n not in possible_chars:
                    n = '#'
                var = n
                if n=='/':
                    var = 'SLASH'
                if n=='.':
                    var = 'PERIOD'
                if n==':':
                    var = 'COLON'
                if n==' ':
                    var = 'SPACE'
                path = letter_folder_path + '/' + f'{var}.txt'
                f = open(path,'r')
                lines = f.readlines()
           
                letter_data.append(lines)
                f.close()
            print("created letters") 
            updated = []
            coordinate=0
            print("creating spaces")
            for letternum in letter_data:
                for p in range(len(letternum)):
                    update=SampleApp.mod_coords(self,'X',letternum[p],.125,coordinate)
                    if '\n' not in update:
                        update = update+'\n'
                    updated.append(update)
                coordinate+=1
            print("creating spaces")
            updated2 = SampleApp.line_rescale(self,updated,rescale_factor)
            print("rescale complete")
            if t==0: 
                offset =updated2
            if t==1:
                offset = SampleApp.XYoffset(self,-.43,-.35,updated2)
            if t==2:
                offset = SampleApp.XYoffset(self,-.43,-.67,updated2)
            if t==3:
                offset = SampleApp.XYoffset(self,3.1,0,updated2)
            if t==4:
                offset = SampleApp.XYoffset(self,3.1,-.35,updated2)
            print("boxes complete")
            for line in offset:
                shifted_program.append(line)
            print("boxes combined")
            shifted_program2 = SampleApp.XYoffset(self,x_shift,y_shift,shifted_program)
            print('origin shifted')
        z_shifted = SampleApp.Zoffset(self,z_shift,shifted_program2)
        print("z shifted")
        full_program = full_program+z_shifted
        print("program done")
            
        full_program.append("G0 Z1.500\n")
        full_program.append("G0 X0.000 Y0.000\n")
        full_program.append('M5\n')
        full_program.append('M2\n')
        f = open(f'{save_file}.txt','w')
        for line in full_program:
            f.write(line)
        f.close()

    def write2(self):
        folder_path="//WC-DC/Engineering/users/Intern Folder/Coby Walmsley/CNC Tag Project/.15 Inch Letters"
        available_chars=['!','#',"A","B",'C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','1','2','3','4','5','6','7','8','9','0','.','/','%',':',';','&','(',')',',','-','+','=',' ']
        data_list=[]
        data_list.append(self.entry1.get())
        data_list.append(self.entry2.get())
        if len(data_list[0])<10:
            print('good 1/5')
            if len(data_list[1])<10:
                print('good 2/5')
                if len(data_list[2])<10:
                    print('good 3/5')
                    if len(data_list[3])<10:
                        print('good 4/5')
                        if len(data_list[4])<12:
                            print('good 5/5')
                            self.collect_letters2("Tag Engraving",data_list,folder_path,available_chars)


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()