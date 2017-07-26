# initialize variables
# two lists to keep track since output is a reverse complement
l_output_seq = [];
l_existing_seq = [];
d_acceptable_values = {"G":"C","g":"c","C":"G","c":"g","A":"T","a":"t","T":"A","t":"a"};
# variables used for statistics
seq_count = 0;
total_char_count = 0;

# loop until ‘done’ is input:
while True:
    # -	get sequence from user
    input_seq = input("Please input a DNA sequence: ");

    if input_seq == "done":
        break;

    # -	check whether sequence is a duplicate
    if input_seq in l_existing_seq:
        # -	alert user if this is the case
        print(input_seq,"is already in the list.");
    else:
        # -	check whether the sequence is valid
        char_count = 0;
        l_invalid_char = [];
        output_seq = "";
        for value in reversed(input_seq):
            if value not in d_acceptable_values:
                l_invalid_char.append(value);
            else:
                # since it's already doing a loop through the seq, reverse complement if it's valid
                output_seq += d_acceptable_values[value];
                # statistics
                char_count += 1;

        # -	alert user if invalid
        if len(l_invalid_char) > 0:
            print("The following characters are invalid:",l_invalid_char);
        else:
            # -	add sequence to list if it is valid and unique
            l_output_seq.append(output_seq);
            l_existing_seq.append(input_seq);
            seq_count += 1;
            total_char_count += char_count;
            print(output_seq,"has been added to the list.");

# print list of sequences
print("Sequences: ");
for seq in l_output_seq:
    print("\t"+seq);
print("-- Statistics --");
print("Number of Sequences :");
print("\t",seq_count);
print("Average Sequence Length :");
print("\t",total_char_count/seq_count,"characters");