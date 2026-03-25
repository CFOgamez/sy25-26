import glob

files = glob.glob("server_dump/*.txt")

# Dictionaries to store filenames for each status
ok_files = []
warn_files = []
error_files = []

# Count how many files have each status
ok_count = 0
warn_count = 0
error_count = 0

for file1 in files:
    with open(file1, "r") as f:
        content = f.read()
        has_ok = "OK" in content
        has_warn = "WARN" in content
        has_error = "ERROR" in content

        if has_ok:
            ok_count += 1
            ok_files.append(file1)
        if has_warn:
            warn_count += 1
            warn_files.append(file1)
        if has_error:
            error_count += 1
            error_files.append(file1)

print(f"Files with OK: {ok_count}")
print(f"Files with WARN: {warn_count}")
print(f"Files with ERROR: {error_count}")

# Give the user the choice to print filenames
choice = input("Print filenames for which status? (OK/WARN/ERROR/none): ").strip().upper()
if choice == "OK":
    print("Files with OK status:")
    for fname in ok_files:
        print(fname)
elif choice == "WARN":
    print("Files with WARN status:")
    for fname in warn_files:
        print(fname)
elif choice == "ERROR":
    print("Files with ERROR status:")
    for fname in error_files:
        print(fname)
else:
    print("No filenames printed.")