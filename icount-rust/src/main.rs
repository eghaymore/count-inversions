use ferris_says::say;
use std::io::{stdout, BufWriter};
use std::io::BufRead;
use std::env;
use std::fs::File;

fn main() {
    let stdout = stdout();
    let fpaths = [r"simple.txt", r"backwards.txt", r"example-2.txt"];
    for fp in fpaths {
        let mut fpath = env::current_dir().expect("Failed to get current directory...");
        fpath.push(r"tests");
        fpath.push(fp);
        println!("Attempting to open test file at:");
        println!("{}", fpath.display());
    
        // Read test file and construct array
        let file = File::open(&fpath).expect("Failed to open test file...");// On error this terminates the main function and therefore the
                                                                            // program, returning the error
        let reader = std::io::BufReader::new(file);
        let mut integers = Vec::new();
        for line in reader.lines() {
            let line = line.expect("Could not read line from file..."); // Handle any I/O error
            let number: i32 = line.trim().parse().expect("Could not parse line in file... is it an integer?"); // Parse the line to an integer
            integers.push(number);
        }
    
        // Driver
        let result = mergesort(&mut integers);
        // Greeting
        let message = format!("Found {} inversions!", result);
        let width = message.chars().count();
        let mut writer = BufWriter::new(stdout.lock());
        say(&message, width, &mut writer).unwrap();
    }
}
fn mergesort(arr: &mut Vec<i32>) -> usize{
    let len = arr.len();
    if len < 2 {
        return 0; // Base case: a vector with 0 or 1 element is already sorted
    }
    let mid = len / 2;
    let mut left_half = arr[0..mid].to_vec();
    let mut right_half = arr[mid..len].to_vec();

    let inv1 = mergesort(&mut left_half);
    let inv2 = mergesort(&mut right_half);

    let inv3 = merge(arr, &mut left_half, &mut right_half);
    return inv1 + inv2 + inv3; // Not yet implemented
}

fn merge(arr: &mut Vec<i32>, left: &Vec<i32>, right: &Vec<i32>) -> usize{
    let mut i = 0; // Index for left_half
    let mut j = 0; // Index for right_half
    let mut k = 0; // Index for arr
    let mut inversions = 0; // Inversion counter

    while i < left.len() && j < right.len() {
        if left[i] <= right[j] {
            arr[k] = left[i];
            i += 1;
        } else {
            arr[k] = right[j];
            j += 1;
            inversions += left.len() - i;
        }
        k += 1;
    }

    // Copy any remaining elements from left_half
    while i < left.len() {
        arr[k] = left[i];
        i += 1;
        k += 1;
    }

    // Copy any remaining elements from right_half
    while j < right.len() {
        arr[k] = right[j];
        j += 1;
        k += 1;
    }
    return inversions;
}
