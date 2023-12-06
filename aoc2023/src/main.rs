use std::collections::HashSet;

fn read_input_from_file() -> String {
    let filename = "./src/inputs/test_input_day2.txt";
    let contents =
        std::fs::read_to_string(filename).expect("Something went wrong reading the file");
    return contents;
}

fn get_current_working_dir() -> std::path::PathBuf {
    let cwd = std::env::current_dir().unwrap();
    println!("The current directory is {}", cwd.display());
    return cwd;
}

fn solution_11() -> u32 {
    let contents = read_input_from_file();
    let mut total = 0;
    for line in contents.lines() {
        println!("{}", line);
        let mut first_digit = 0;
        let mut last_digit = 0;
        for c in line.chars() {
            if c.is_digit(10) {
                if first_digit == 0 {
                    first_digit = c.to_digit(10).unwrap();
                }
                last_digit = c.to_digit(10).unwrap();
            }
        }
        total = total + first_digit * 10 + last_digit;
    }
    return total;
}

fn solution_12() -> u32 {
    let contents = read_input_from_file();
    let mut total = 0;
    let digit_words = HashSet::from([
        "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
    ]);

    for line in contents.lines() {
        println!("{}", line);
        let mut first_digit = 0;
        let mut last_digit = 0;
        for c in line.chars() {
            if c.is_digit(10) {
                if first_digit == 0 {
                    first_digit = c.to_digit(10).unwrap();
                }
                last_digit = c.to_digit(10).unwrap();
            }
        }
        total = total + first_digit * 10 + last_digit;
    }
    return total;
}

fn main() {
    let answer_11 = solution_11();
    println!("total: {}", answer_11);
}
